class CustomException(Exception):
    def __init__(self, message="Произошла ошибка"):
        self.message = message
        super().__init__(self.message)

# Использование исключения при делении на ноль
def divide_numbers(a, b):
    try:
        if b == 0:
            raise CustomException("Деление на ноль недопустимо")
        result = a / b
        print(f"Результат деления: {result}")
    except CustomException as ce:
        print(f"Ошибка: {ce}")

# Использование исключения при вводе отрицательного числа
def get_positive_number():
    try:
        number = int(input("Введите положительное число: "))
        if number < 0:
            raise CustomException("Введено отрицательное число")
        print(f"Введенное положительное число: {number}")
    except CustomException as ce:
        print(f"Ошибка: {ce}")

# Тесты
divide_numbers(10, 0)
get_positive_number()
