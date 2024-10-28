import json
import logging
from typing import Any
import csv

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/utils.log",
    # filename="utils.log",
    filemode="w",
)
auth_logger = logging.getLogger("app.auth")
# logger = logging.getLogger(__name__)
# file_handler = logging.FileHandler('utils.log')
# logger.addHandler(file_handler)
# logger.setLevel(logging.INFO)


def get_transactions_dictionary(path: str) -> dict | Any:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        # with open(path, "r", "operations.json", encoding='utf-8') as operations:
        with open(path, "r", encoding="utf-8") as operations:

            try:
                auth_logger.info("Информация по счету")
                list_trans = json.load(operations)
                return list_trans
            except json.JSONDecodeError:
                list_trans = []
                auth_logger.info("Информация по счету не удачно")
                return list_trans
    except FileNotFoundError:
        list_trans = []
        auth_logger.info("Файл поврежден")
        return list_trans
        # говорит о возрощений пипа list


def get_transactions_dictionary_csv(csv_path: str) -> list[dict]:
    """Aункция пути до CSV-файла и возвращает список словарей с данными о финансовых транзакциях"""

    transaction_list = []
    try:
        with open(csv_path, encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file, delimiter=";")
            next(reader)
            for row in reader:
                if row:
                    id_, state, date, amount, currency_name, currency_code, from_, to, description = row
                    transaction_list.append(
                        {
                            "id": str(id_),
                            "state": state,
                            "date": date,
                            "operationAmount": {
                                "amount": str(amount),
                                "currency": {"name": currency_name, "code": currency_code},
                            },
                            "description": description,
                            "from": from_,
                            "to": to,
                        }
                    )
    except Exception:
        return []
    return transaction_list


def get_transactions_dictionary_excel(excel_path: str) -> list[dict]:
    """FAункция пути до EXCEL-файла и возвращает список словарей с данными о финансовых транзакциях"""

    transaction_list = []
    try:
        excel_data = pd.read_excel(excel_path)
        len_, b = excel_data.shape
        for i in range(len_):
            if excel_data["id"][i]:
                transaction_list.append(
                    {
                        "id": str(excel_data["id"][i]),
                        "state": excel_data["state"][i],
                        "date": excel_data["date"][i],
                        "operationAmount": {
                            "amount": str(excel_data["amount"][i]),
                            "currency": {
                                "name": excel_data["currency_name"][i],
                                "code": excel_data["currency_code"][i],
                            },
                        },
                        "description": excel_data["description"][i],
                        "from": excel_data["from"][i],
                        "to": excel_data["to"][i],
                    }
                )
            else:
                continue
    except Exception:
        return []
    return transaction_list


if __name__ == "__main__":
    wine_reviews = pd.read_csv("transactions.csv")
    excel_data = pd.read_excel("transactions_excel.xlsx")