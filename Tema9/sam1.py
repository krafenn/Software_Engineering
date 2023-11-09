class Tomato:
    states = {
        1: "Отсутствует",
        2: "Цветение",
        3: "Зеленый",
        4: "Красный"
    }

    def __init__(self, index):
        # Инициализация экземпляра класса Tomato
        self._index = index  # Уникальный индекс помидора
        self._state = 1  # Начальная стадия - Отсутствует

    def grow(self):
        # Метод для созревания томата на следующую стадию
        if self._state < 4:
            self._state += 1
        else:
            print("Томат уже созрел")

    def is_ripe(self):
        # Метод для проверки, созрел ли томат (достиг последней стадии созревания)
        return self._state == 4


class TomatoBush:
    def __init__(self, num):
        # Инициализация куста с томатами
        self.tomatoes = [Tomato(index) for index in range(1, num + 1)]  # Создание списка томатов

    def grow_all(self):
        # Метод для созревания всех томатов на кусте
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        # Метод для проверки, все ли томаты на кусте созрели
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        # Метод для сбора урожая (очистка списка томатов)
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        # Инициализация садовника
        self.name = name  # Имя садовника
        self._plant = plant  # Растение, за которым ухаживает садовник

    def work(self):
        # Метод, который заставляет садовника работать (растение становится более зрелым)
        self._plant.grow_all()

    def harvest(self):
        # Метод для сбора урожая
        if self._plant.all_are_ripe():
            print("Урожай собран!")
            self._plant.give_away_all()  # Очистка списка томатов после сбора урожая
        else:
            print("Пока не все томаты созрели. Ждите немного.")

    @staticmethod
    def knowledge_base():
        # Статический метод, выводящий справку по садоводству
        print("Справка по садоводству:")
        print("1. Регулярный полив и удобрение помогают растениям расти здоровыми.")
        print("2. Внимательно следите за созреванием плодов для своевременного сбора урожая.")

# Тесты
Gardener.knowledge_base()  # Справка по садоводству

bush = TomatoBush(5)  # Создание куста с 5 томатами
gardener = Gardener("Иван", bush)  # Создание садовника

gardener.work()  # Уход за растением
gardener.harvest()  # Попытка собрать урожай

gardener.work()  # Еще немного ухода за растением
gardener.work()  # Еще немного ухода за растением
gardener.harvest()  # Сбор урожая после полного созревания
