# Импортируем модуль datetime для работы с датой и временем и модуль sqrt из библиотеки math для вычисления квадратного корня
from datetime import datetime
from math import sqrt

# Определение функции main, которая принимает произвольное количество именованных аргументов
def main(**kwargs):
    # Проход по входным кортежам
    for key in kwargs.items():
        # Вычисляем квадратный корень суммы квадратов элементов списка, переданного в значении аргумента
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        # Выводим результат на экран
        print(result)

# Проверяем, что код выполняется как самостоятельная программа (а не импортируется как модуль)
if __name__ == '__main__':
    # Запоминаем текущее время перед выполнением функции main
    start_time = datetime.now()

    # Вызываем функцию main с передачей именованных аргументов (словарей), каждый из которых представляет координаты точки
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )

    # Вычисляем время, прошедшее с начала выполнения программы
    time_costs = datetime.now() - start_time
    # Выводим время выполнения программы на экран
    print(f"Время выполнения программы - {time_costs}")
