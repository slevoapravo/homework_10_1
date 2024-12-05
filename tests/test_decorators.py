import os

import pytest

from src.decorators import log


@pytest.fixture(scope='function', autouse=True)
def cleanup_log_file():
    # Очистка файла перед и после теста
    log_filename = "test_log.txt"
    if os.path.exists(log_filename):
        os.remove(log_filename)
    yield
    if os.path.exists(log_filename):
        os.remove(log_filename)


def test_my_function_success(capsys):
    @log(filename="test_log.txt")
    def my_function(x, y):
        return x + y

    # Проверка корректного выполнения функции
    result = my_function(1, 2)
    captured = capsys.readouterr()

    assert result == 3, "Ошибка в вычислении результата функции"
    assert "my_function called with args: (1, 2), kwargs: {}. Result: 3\n" in captured.out
#        "Лог не содержит правильной информации о вызове функции"


def test_my_function_error(capsys):
    @log(filename="test_log.txt")
    def my_function(x, y):
        return x + y

    # Проверка ошибки
    with pytest.raises(TypeError):
        my_function(0, 2)

    captured = capsys.readouterr()
    assert "my function error: " in captured.out, "Лог не содержит информации об ошибке"
