class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def make_sound(self):
        print("Мяу!")
class PersianCat(Cat):
    def __init__(self, name, age, color, fur_length):
        super().__init__(name, age, color)
        self.fur_length = fur_length

    def make_sound(self):
        print("Мур!")

def cat_sounds(cat):
    cat.make_sound()

my_cat = Cat("Барсик", 3, "серый")
my_persian_cat = PersianCat("Мурзик", 4, "белый", "длинная")
cat_sounds(my_cat)
cat_sounds(my_persian_cat)
