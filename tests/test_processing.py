from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def executed_transactions() -> List[Dict[str, Any]]:
    """Фикстура для списка транзакций с состоянием EXECUTED"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def non_executed_transactions() -> List[Dict[str, Any]]:
    """Фикстура для списка транзакций с состоянием, отличным от EXECUTED"""
    return [
        {"id": 12345678, "state": "PENDING", "date": "2019-07-03T18:35:29.512364"},
        {"id": 87654321, "state": "CANCELLED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.mark.parametrize("state", ["EXECUTED"])
def test_filter_by_state(executed_transactions: List[Dict[str, Any]], state: str) -> None:
    """Тестирование фильтрации транзакций по состоянию"""
    assert filter_by_state(executed_transactions) == state


@pytest.mark.parametrize("transactions, expected", [
    ([
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ], "EXECUTED"),
])


def test_sort_by_date(transactions: List[Dict[str, Any]], expected: str) -> None:
    """Тестирование сортировки транзакций по дате"""
    assert sort_by_date(transactions) == expected
