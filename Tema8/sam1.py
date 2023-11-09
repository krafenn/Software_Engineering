class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Кот по имени {self.name}, возраст {self.age} год(а).")

my_cat = Cat("Барсик", 3)
another_cat = Cat("Мурзик", 5)
my_cat.info()
another_cat.info()