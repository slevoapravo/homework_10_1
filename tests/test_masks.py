from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


# Фикстура для корректных данных карт
@pytest.fixture
def valid_card_data():
    return [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7619804582344591", "7619 80** **** 4591"),
    ]


# Фикстура для некорректных данных карт
@pytest.fixture
def invalid_card_data():
    return "4534534gdfgf"


# Фикстура для корректных данных счетов
@pytest.fixture
def valid_account_data():
    return [
        ("73654108430135878796", "** 8796"),
        ("73654108430135874305", "** 4305"),
    ]


def test_get_mask_card_number(valid_card_data, invalid_card_data):
    """Тестирование маскировки номера карты"""
    # Проверка некорректных данных
    assert get_mask_card_number(invalid_card_data) == "Некорректные данные"

    # Проверка корректных данных
    for card_number, mask_number in valid_card_data:
        assert get_mask_card_number(card_number) == mask_number


def test_get_mask_account(valid_account_data):
    """Тестирование маскировки номера счета"""
    for number_account, hide_account in valid_account_data:
        assert get_mask_account(number_account) == hide_account
