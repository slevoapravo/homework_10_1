from typing import Any

import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def accounts_data():
    return [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет ** 4305"),
    ]


@pytest.fixture
def date_data():
    return ("2024-09-30T02:26:18.671407", "30.09.2024")


def test_mask_account_card(accounts_data: Any) -> None:
    """Тестирование маскировки счета и номера карты"""
    for account, account_hide in accounts_data:
        assert mask_account_card(account) == account_hide


def test_get_date(date_data: Any) -> None:
    """Тестирование формата даты"""
    date, new_date = date_data
    assert get_date(date) == new_date
