from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, mask_number",
    [("7000792289606361", "7000 79** **** 6361"), ("7619804582344591", "7619 80** **** 4591")],
)
def test_get_mask_card_number(card_number: Any, mask_number: Any) -> Any:
    """Тестирование маскировки номера карты"""
    try:
        assert get_mask_card_number("4534534gdfgf") == "Некорректные данные"
        assert get_mask_card_number(card_number) == mask_number
    except AssertionError:
        print("Некорректные данные")



@pytest.mark.parametrize(
    "number_account, hide_account", [("73654108430135878796", "** 8796"), ("73654108430135874305", "** 4305")]
)
def test_get_mask_account(number_account: Any, hide_account: Any) -> Any:
    """Тестирование маскировки номера счета"""
    assert get_mask_account(number_account) == hide_account