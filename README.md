# Банковские операции
## Описание проекта
Программа создана для фильтрации и сортировки банковских счетов по дате и оплате.
## Project dependencies:
* The program uses the version Python 3.12.
* flake8 = "^7.1.1"
* mypy = "^1.11.2"
* black = "^24.8.0"
* isort = "^5.13.2"

## Функции, которые мы будем использовать:
* Функция скрывающая номер карты и счета
* Функция сортировки по дате
* Функция фильтрации в операциях по счетам
* Функция считывания финансовых операций из CSV- и XLSX-файлов.
## Тестирование проекта

Pytest

#### Структура проекта:

1. tests/ - папка, в которой содержатся тесты проекта.
2. src/ - папка, содержащая файлы с функциями проекта.
3. .venv - виртуальное окружение, содержащее библиотеки и скрипты.

## Использование:

1. Модуль masks.py принимает на вход номер карты или счета и маскирует их.
2. Модуль widget.py принимает наименование карты или счет и номер и возвращает замаскированный номер.
3. Модуль processing.py принимает список операций и возвращает отсортированные списки.
4. Модуль generators.py сортирует списки операций и генерирует номера карт.
5. Модуль decorators.py  логирует функции маскирования номеров карт и счетов, и вывода суммы транзакции в рублях
6. Модуль import_data.py  может работать с файлами в форматах json, CSV и excel.
## 1.Инструкция по установке
Чтобы скачать репозиторий:

## 2.Структура проекта

1. tests/ - папка, в которой содержатся тесты проекта.
2. src/ - папка, содержащая файлы с функциями проекта.
3. .venv - виртуальное окружение, содержащее библиотеки и скрипты.

## 3. Модули 
1. Модуль masks.py принимает на вход номер карты или счета и маскирует их.
2. Модуль widget.py принимает наименование карты или счет и номер и возвращает замаскированный номер.
3. Модуль processing.py принимает список операций и возвращает отсортированные списки.
4. Модуль generators.py сортирует списки операций и генерирует номера карт.
5. Модуль decorators.py используется для размещения декораторов, где реализован декоратор log, который будет автоматически регистрировать детали выполнения функций.

## 4.Установить не обходимые зависимости

## 5.Команда проекта:

## 6.Контакт для связи с командой разработки:

## 7.Источники