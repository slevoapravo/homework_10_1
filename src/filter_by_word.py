from collections import defaultdict


import re

def str_sort(filtered_transactions: list[dict], word: str) -> list[dict]:
    """
    Фильтрация и сортировка списка словарей по наличию подстроки в поле "description".

    Args:
        filtered_transactions: Список словарей, где каждый словарь представляет транзакцию
                               и содержит ключ "description" (строка).  Если ключа нет,
                               значение по умолчанию - пустая строка.
        word: Подстрока, по которой осуществляется поиск в поле "description".

    Returns:
        Отсортированный список словарей, содержащих транзакции, в описании которых
        найдена заданная подстрока.  Возвращает пустой список, если совпадений нет.
        Сортировка производится по полю "description" (лексикографически).

    Raises:
        TypeError: Если `filtered_transactions` не является списком словарей.
        TypeError: Если `word` не является строкой.

    """
    if not isinstance(filtered_transactions, list):
        raise TypeError("filtered_transactions must be a list of dictionaries.")
    if not all(isinstance(item, dict) for item in filtered_transactions):
        raise TypeError("filtered_transactions must be a list of dictionaries.")
    if not isinstance(word, str):
        raise TypeError("word must be a string.")

    found_operations = [
        op for op in filtered_transactions if re.search(word, op.get("description", ""))
    ]
    found_operations.sort(key=lambda x: x.get("description", "")) # Сортировка по description
    return found_operations




# def filter_transactions(transactions_list: list[dict], search_string: str) -> list[dict]:
#     """
#     Функция для фильтрации списка словарей с операциями на основе строки поиска.
#     :param transactions_list: список словарей, где каждый словарь представляет собой операцию
#     :param search_string: строка для поиска в описаниях операций
#     :return: список словарей, в которых описание содержит строку поиска
#     """
#     # Компилируем регулярное выражение для поиска
#     pattern = re.compile(re.escape(search_string), re.IGNORECASE)
#
#     # Фильтруем список операций
#     filtered_transactions = [
#         data for data in transactions_list if "description" in data and pattern.search(data["description"])
#     ]
#     return filtered_transactions


def count_operations_by_category(transactions_list: list[dict], categories: list[str]) -> dict[str, int]:
    """Функция, принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории."""

    # Создаем словарь для хранения количества операций по категориям
    category_count = defaultdict(int)

    # Проходим по каждому словарю в списке transactions
    for transaction in transactions_list:
        description = transaction.get("description", "").lower()

        # Проходим по каждой категории и проверяем, соответствует ли описание операции категории
        for category in categories:

            # Используем регулярное выражение для поиска категории в описании
            if re.search(re.escape(category.lower()), description):
                category_count[category] += 1  # Увеличиваем счетчик для найденной категории

    return dict(category_count)  # Преобразуем defaultdict обратно в обычный словарь для возвращения