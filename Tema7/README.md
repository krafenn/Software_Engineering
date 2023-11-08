# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил(а):
- Пчелкин Дмитрий Андреевич
- ПИЭ-21-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |
| Задание 7 | + |
| Задание 8 | + |
| Задание 9 | + |
| Задание 10 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema7/Tema7/pic/lab1.png)

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readline())
f.close()
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema7/Tema7/pic/lab2.png)

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readlines())
f.close()
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema7/Tema7/pic/lab3.png)

## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    print(f.readlines())
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema7/Tema7/pic/lab4.png)

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    for line in f:
        print(line)
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema7/Tema7/pic/lab5.png)

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```python
with open('input.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema7/Tema7/pic/lab6.png)

## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.

lab47.py:
```python
lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema7/Tema7/pic/lab7.png)

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).

```python
import os


def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)


print_docs('/Users/Andrey/Downloads')
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema7/Tema7/pic/lab8.png)

## Лабораторная работа №9
### Документ «input.txt» содержит следующий текст: 
Приветствие 
Спасибо 
Извините 
Пожалуйста 
До свидания 
Ты готов? 
Как дела? 
С днем рождения! 
Удача! 
Я тебя люблю. 
Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных.

```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words


print(longest_words('input.txt'))
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema7/Tema7/pic/lab9.png)

## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами: 
• № - номер по порядку (от 1 до 300);
• Секунда – текущая секунда на вашем ПК;
• Микросекунда – текущая миллисекунда на часах. 
Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema7/Tema7/pic/lab10.png)


## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация

###Скриншот файла со статьей:
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema7/Tema7/pic/sam12.png)

```python
from collections import Counter
import string

with open('inputsam.txt', 'r', encoding='utf-8') as file:
    content = file.read().lower()

translator = str.maketrans('', '', string.punctuation)
content = content.translate(translator)
words = content.split()
word_count = Counter(words)
most_common_word = word_count.most_common(1)[0]

print(f"Общее количество слов в статье: {len(words)}")
print(f"Самое часто встречающееся слово: '{most_common_word[0]}' (встречается {most_common_word[1]} раз)")
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema7/Tema7/pic/sam1.png)

## Выводы

Данный код выполняет анализ текстового файла 'inputsam.txt'. Он считывает файл, преобразует текст в нижний регистр, удаляет знаки пунктуации и разделяет текст на слова. Используя модуль Counter из библиотеки collections, он подсчитывает количество вхождений каждого слова. Затем определяется наиболее часто встречающееся слово и его количество в тексте. Результаты выводятся, указывая общее количество слов в тексте и самое часто встречающееся слово, включая количество его вхождений.
  
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

###Скриншот файла с учетом расходов:
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema7/Tema7/pic/sam21.png)

```python
def add_expense(amount, category, file):
    record = f"{amount} {category}\n"
    with open(file, 'a', encoding='utf-8') as expense_file:
        expense_file.write(record)
    print("Расход успешно записан!")

def show_expenses(file):
    try:
        with open(file, 'r') as expense_file:
            expenses = expense_file.readlines()
            if expenses:
                print("\nСуществующие расходы:")
                for expense in expenses:
                    print(expense.strip())
            else:
                print("\nНет сохраненных расходов.")
    except FileNotFoundError:
        print("\nФайл не найден или расходы не сохранены.")

expenses_file = "расходы.txt"

print("Программа учета расходов")
while True:
    print("\nВыберите действие:")
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Выйти")
    choice = input("Введите номер действия: ")

    if choice == "1":
        amount = input("Введите сумму расхода: ")
        category = input("Введите категорию расхода: ")
        add_expense(amount, category, expenses_file)
    elif choice == "2":
        show_expenses(expenses_file)
    elif choice == "3":
        print("До свидания!")
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema7/Tema7/pic/sam2.png)

## Выводы

Данный код представляет программу учета расходов, включающую две функции: add_expense, которая добавляет записи о расходах в указанный файл, и expenses_show, которая выводит сохраненные расходы из файла. В интерфейсной части программы пользователю предлагается выбор действий: добавить расход, показать все расходы или выйти из программы. В зависимости от выбора пользователя выполняются соответствующие действия, продолжая работу до момента, когда пользователь выберет выход из программы.
  
## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк. 
• Текст в файле: 
Beautiful is better than ugly. 
Explicit is better than implicit. 
Simple is better than complex. 
Complex is better than complicated. 
• Ожидаемый результат: 
Input file contains: 108 
letters 20 words 
4 lines

```python
with open('input.txt', 'r') as file:
    content = file.read()

letters_count = 0
word_count = len(content.split())
line_count = content.count('\n') + 1

for char in content:
    if char.isalpha() and char.isascii():
        letters_count += 1

print(letters_count, "letters")
print(word_count, "words")
print(line_count, "lines")

```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema7/Tema7/pic/sam3.png)

## Выводы

Данный код открывает файл 'input.txt' для чтения, читает его содержимое, и выполняет три подсчета: количество слов в тексте, количество строк по символам новой строки, и общее количество букв. Для подсчета букв код проходит по каждому символу текста, проверяя, является ли он буквой и ASCII-символом. По завершении, выводится количество букв, слов и строк в файле.
  
## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****. 
• Запрещенные слова: 
hello email python the exam wor is 
• Предложение для проверки: 
Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!! 
• Ожидаемый результат: 
*****, ***ld! ****** ** *** programming language of *** future. My ***** **.... ****** ** awesome!!!!

```python
import re

def censor_words(sentence, banned_words):
    for word in banned_words:
        sentence = re.sub(rf'\b{re.escape(word)}\b', '*' * len(word), sentence, flags=re.IGNORECASE)
    return sentence

input_sentence = 'Hello, world! Python IS the programming language of thE future. My EMAIL is.... \nPYTHON is awesome!!!!'

with open('input.txt', 'r') as file:
    banned = file.readline().split()

censored_text = censor_words(input_sentence, banned)
print(censored_text)
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema7/Tema7/pic/sam4.png)

## Выводы

Данный код содержит функцию censor_words, которая заменяет запрещенные слова в предложении символами '', соответствующими их длине. Эта функция использует модуль re для замены каждого запрещенного слова из списка banned_words в предложении sentence. Код также читает список запрещенных слов из файла 'input.txt' и затем применяет функцию censor_words к предложению input_sentence, выводя на экран цензурированный текст, где каждое запрещенное слово заменено символами '' той же длины.
  
## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

###Задание:
###Напишите программу, которая считает количество слов в предоставленном текстовом файле. Программа должна открывать указанный файл, а затем анализировать его содержимое для определения общего количества слов. Текстовый файл содержит предложения на разных строках. Необходимо прочитать этот файл, определить количество слов, и вывести результат, показывающий общее число слов в файле.

```python
file_name = 'text.txt'

try:
    with open(file_name, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        print(f"Количество слов в файле '{file_name}': {word_count}")

except FileNotFoundError:
    print(f"Файл '{file_name}' не найден")
```

### Результат.
![Меню](https://github.com/krafenn/Software_Engineering/blob/Tema7/Tema7/pic/sam5.png)

## Выводы

Данный код начинается с попытки открыть файл с именем 'text.txt' для чтения. В случае успешного открытия файла, его содержимое считывается и разделяется на слова при помощи метода split(). Затем подсчитывается количество слов в файле путем определения длины списка words и выводится на экран вместе с информацией о количестве слов в файле 'text.txt'. Если файл не найден, программа выводит сообщение об ошибке, указывая на отсутствие файла с именем 'text.txt'.

## Общие выводы по теме

В данной теме я познакомился с работой с файлами языка Python.
