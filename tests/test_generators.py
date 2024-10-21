import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2022-07-29T14:05:01.413456",
        "operationAmount": {
            "amount": "2000.00",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2024-07-01T13:21:01.206564",
        "operationAmount": {
            "amount": "30000.00",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2021-04-21T15:15:45.125475",
        "operationAmount": {
            "amount": "40000.00",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2006-04-21T015:27:14.123456",
        "operationAmount": {
            "amount": "50000.00",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2020-10-15T20:13:11.147258",
        "operationAmount": {
            "amount": "99000.00",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def test_transaction_descriptions():
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


@pytest.mark.parametrize('index, expected', [(0, 'Перевод организации'), (1, 'Перевод со счета на счет')])
def test_transaction_descriptions_3(index, expected):
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions[index] == expected


def test_filter_by_currency():
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == 939719570
    assert next(generator) == 142264268
    assert next(generator) == 895315941
    generator_1 = filter_by_currency(transactions, "RUB")
    assert next(generator_1) == 873106923
    assert next(generator_1) == 594226727


def test_card_number_generator():
    generator = card_number_generator(3, 7)
    assert (next(generator)) == "3000 0000 0000 0000"
    assert (next(generator)) == "4000 0000 0000 0000"
    assert (next(generator)) == "5000 0000 0000 0000"
    assert (next(generator)) == "6000 0000 0000 0000"


@pytest.fixture
def sample_transactions():
    """Фикстура для тестовых данных о транзакциях."""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2022-07-29T14:05:01.413456",
            "operationAmount": {
                "amount": "2000.00",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2022-07-29T14:05:01.413456",
            "operationAmount": {
                "amount": "1500.00",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 75106830613657916953",
            "to": "Счет 11776614605963066703",
        },]
