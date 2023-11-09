# Тема 8. Основы объектно-ориентированного программирования
Отчет по Теме #8 выполнил:
- Пчелкин Дмитрий Андреевич
- ПИЭ-21-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Создайте класс «Car» с атрибутами производитель и модель. Создайте объект этого класса. Напиши комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.

```python
class Car:
    def __init__(self, make, model):
        self.make = make # Устанавливает производителя автомобиля.
        self.model = model # Устанавливает модель автомобиля.
        

my_car = Car("Toyota", "Corolla") # Создание экземпляра класса Car с указанным производителем "Toyota" и моделью "Corolla".
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema8/Tema8/pic/lab1.png)

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину «поехать». Напиши комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self.make = make # Устанавливает производителя автомобиля.
        self.model = model # Устанавливает модель автомобиля.

    def drive(self):
        print(f"Driving the {self.make} {self.model}") # Выводит сообщение о том, что осуществляется езда на автомобиле с указанным производителем и моделью.

my_car = Car("Toyota", "Corolla") # Создание экземпляра класса Car с производителем "Toyota" и моделью "Corolla".
my_car.drive() # Вызов метода drive() для этого экземпляра класса, что приводит к выводу сообщения о езде на автомобиле "Toyota Corolla".
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema8/Tema8/pic/lab2.png)

## Лабораторная работа №3
### Создайте новый класс «ElectricCar» c методом «charge» и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Напиши комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self.make = make # Устанавливает производителя автомобиля.
        self.model = model # Устанавливает модель автомобиля.

    def drive(self):
        print(f"Driving the {self.make} {self.model}") # Выводит сообщение о том, что происходит езда на автомобиле с указанным производителем и моделью.

my_car = Car("Toyota", "Corolla") # Создание экземпляра класса Car с производителем "Toyota" и моделью "Corolla".
my_car.drive() # Вызов метода drive() для этого экземпляра класса, что приводит к выводу сообщения о езде на автомобиле "Toyota Corolla".

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model) # Вызов конструктора родительского класса для установки производителя и модели.
        self.battery_capacity = battery_capacity # Устанавливает емкость батареи.

    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh") # Выводит сообщение о зарядке автомобиля с указанным производителем, моделью и емкостью батареи.


my_electric_car = ElectricCar("Tesla", "Model S", 75) # Создание экземпляра класса ElectricCar с производителем "Tesla", моделью "Model S" и емкостью батареи 75.
my_electric_car.drive() # Вызов метода drive() для объекта ElectricCar, выводящий сообщение о езде на автомобиле "Tesla Model S".
my_electric_car.charge() # Вызов метода charge() для объекта ElectricCar, выводящий сообщение о зарядке автомобиля "Tesla Model S" с емкостью батареи 75 kWh. 
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema8/Tema8/pic/lab3.png)

## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напиши комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self.make = make # Устанавливает производителя автомобиля.
        self.model = model # Устанавливает модель автомобиля.

    def drive(self):
        print(f"Driving the {self.make} {self.model}") # Выводит сообщение о том, что происходит езда на автомобиле с указанным производителем и моделью.

my_car = Car("Toyota", "Corolla") # Создание экземпляра класса Car с производителем "Toyota" и моделью "Corolla".
print(my_car.make) # Выводит производителя автомобиля: "Toyota".
my_car.drive() # Вызов метода drive() для этого экземпляра класса, выводящий сообщение о езде на автомобиле "Toyota Corolla".
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema8/Tema8/pic/lab4.png)

## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс «Shape», а также еще два класса «Rectangle» и «Circle». Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напиши комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Shape:
    def area(self):
        pass # Абстрактный метод, который должен быть переопределен в подклассах.

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width # Устанавливает ширину прямоугольника.
        self.height = height # Устанавливает высоту прямоугольника.

    def area(self):
        return self.width * self.height # Возвращает площадь прямоугольника.


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius # Устанавливает радиус круга.

    def area(self):
        return 3.14 * self.radius * self.radius # Возвращает площадь круга.
    
rectangle = Rectangle(4,5) # Создание прямоугольника со шириной 4 и высотой 5.
circle = Circle(3) # Создание круга с радиусом 3.

print(rectangle.area()) # Выводит площадь прямоугольника
print(circle.area()) # Выводит площадь круга
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema8/Tema8/pic/lab5.png)


## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться от тех, что указаны в теоритическом материале (методичке) и лаборатоных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema8/Tema8/pic/sam1.png)

## Выводы

Данный код создает класс Cat, где каждый кот имеет имя и возраст. Он содержит метод info, который выводит информацию о коте. Затем создаются два кота: "Барсик" возрастом 3 года и "Мурзик" возрастом 5 лет. Метод info вызывается для каждого кота, выводя их данные - имя и возраст.

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться от тех, что указаны в теоритическом материале (методичке) и лаборатоных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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

my_cat = Cat("Барсик", 3, "серый")

my_cat.info()

my_cat.fall_asleep()
my_cat.fall_asleep()
my_cat.wake_up()
my_cat.wake_up()
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema8/Tema8/pic/sam2.png)

## Выводы

Данный код создает класс Cat с атрибутами имени, возраста, цвета и состояния сна. Метод info выводит информацию о коте, а fall_asleep и wake_up позволяют коту заснуть и проснуться соответственно. Программа создает кота "Барсик", выводит его информацию, и демонстрирует способность кота засыпать и просыпаться, проверяя его текущее состояние.
  
## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться от тех, что указаны в теоритическом материале (методичке) и лаборатоных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema8/Tema8/pic/sam3.png)

## Выводы

Данный код определяет два класса: Cat и PersianCat, где PersianCat наследует от Cat. Cat содержит атрибуты и методы для управления информацией и состоянием кота, включая способность усыпления и пробуждения. PersianCat расширяет класс Cat, добавляя атрибут длины шерсти и переопределяя метод info, чтобы выводить дополнительную информацию о персидском коте. Программа создает объект my_persian_cat класса PersianCat с определенными характеристиками и демонстрирует вывод информации о персидском коте, а также его возможность усыпления.
  
## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться от тех, что указаны в теоритическом материале (методичке) и лаборатоных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema8/Tema8/pic/sam4.png)

## Выводы

Данный код создает класс Cat, включающий атрибуты имени, возраста и цвета, а также методы для вывода информации о коте, усыпления и пробуждения. Атрибут _is_sleeping представляет состояние сна кота. Создается экземпляр my_cat класса Cat с именем "Барсик", возрастом 3 года и серым цветом. Затем вызываются методы для вывода информации о коте, попыток усыпления, а затем пробуждения.
  
## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должнен отличаться от того, что указаны в теоритическом материале (методичке) и лаборатоных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

###Напишите программу, которая вычисляет среднее время, проведенное пользователями на веб-сайте в каждый день недели. Программа принимает список кортежей, где каждый кортеж содержит информацию о времени, проведенном на сайте в определенный день недели. Функция должна возвращать список кортежей с названием дня недели и средним временем, проведенным в этот день.

```python
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
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema8/Tema8/pic/sam5.png)

## Выводы

Данный код содержит классы Cat и PersianCat, где PersianCat является подклассом Cat. У обоих классов есть метод make_sound, который выводит звук, характерный для каждого типа кота. Функция cat_sounds принимает объект кота в качестве аргумента и вызывает его метод make_sound, выводя звук, свойственный этому коту. Создаются объекты my_cat и my_persian_cat с различными характеристиками, и для каждого вызывается функция cat_sounds, выводя соответствующий звук для каждого типа кота.

## Общие выводы по теме

В данной теме я познакомился с основами объектно-ориентированного программирования языка Python.
