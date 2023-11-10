class CustomDecorator:
    # Инициализация декоратора
    def __init__(self, func):
        self.func = func

    # Реализация вызова декоратора
    def __call__(self, *args, **kwargs):
        print(f"До выполнения функции {self.func.__name__}")
        # Вызов оригинальной функции
        result = self.func(*args, **kwargs)
        print(f"После выполнения функции {self.func.__name__}")
        return result

# Функция 1: умножение
@CustomDecorator
def multiply(a, b):
    result = a * b
    print(f"Результат умножения: {result}")
    return result

# Функция 2: возведение в степень
@CustomDecorator
def power(base, exponent):
    result = base ** exponent
    print(f"Результат возведения в степень: {result}")
    return result

# Тесты
multiply(3, 4)
power(2, 3)
