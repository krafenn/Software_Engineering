class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self._is_sleeping = False

    def info(self):
        print(f"Кот по имени {self.name}, возраст {self.age} год(а), цвет - {self.color}.")

    def fall_asleep(self):
        if not self._is_sleeping:
            self._is_sleeping = True
            print(f"{self.name} засыпает...")
        else:
            print(f"{self.name} уже спит.")

    def wake_up(self):
        if self._is_sleeping:
            self._is_sleeping = False
            print(f"{self.name} просыпается.")
        else:
            print(f"{self.name} уже бодрствует.")

my_cat = Cat("Барсик", 3, "серый")
my_cat.info()
my_cat.fall_asleep()
my_cat.fall_asleep()
my_cat.wake_up()
my_cat.wake_up()