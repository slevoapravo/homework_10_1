from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Логирует вызов функции и ее результат в файл или в консоль
    :param filename: Путь к файлу для записи логов. Если не указан, логи выводятся в консоль.
    :return: Декоратор для логирования вызовов функции.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} called with args: {args}, kwargs: {kwargs}. Result: {result}"

                # Логирование
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)

                return result  # Возвращаем результат
            except Exception as e:
                error_message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"

                # Логирование ошибки
                if filename:
                    with open(filename, "a") as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)

                raise  # Поднимаем исключение дальше

        return wrapper

    return decorator


@log(filename="test_log.txt")
def my_function(x: int, y: int) -> int:
    return x + y


# Пример вызова функции с корректными аргументами
try:
    print(my_function(1, 2))  # Выводит 3
    print(my_function(1, "t"))  # Выкидывает ошибку
except Exception as e:
    print(f"An error occurred: {e}")
