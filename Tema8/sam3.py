class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.is_sleeping = False

    def info(self):
        print(f"Кот по имени {self.name}, возраст {self.age} год(а), цвет - {self.color}.")

    def fall_asleep(self):
        if not self.is_sleeping:
            self.is_sleeping = True
            print(f"{self.name} засыпает...")
        else:
            print(f"{self.name} уже спит.")


    def wake_up(self):
        if self.is_sleeping:
            self.is_sleeping = False
            print(f"{self.name} просыпается.")
        else:
            print(f"{self.name} уже бодрствует.")
class PersianCat(Cat):
    def __init__(self, name, age, color, fur_length):
        super().__init__(name, age, color)
        self.fur_length = fur_length

    def info(self):
        print(f"Персидский кот по имени {self.name}, возраст {self.age} год(а), цвет - {self.color}, длина шерсти - {self.fur_length}.")

my_persian_cat = PersianCat("Мурзик", 4, "белый", "длинная")
my_persian_cat.info()
my_persian_cat.fall_asleep()