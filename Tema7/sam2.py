# Открыть файл для чтения
with open('input.txt', 'r') as file:
    content = file.read()

# Инициализация счетчиков
latin_letters_count = 0
word_count = len(content.split())  # Подсчитать слова через разделение пробелами
line_count = content.count('\n') + 1  # Подсчитать строки по символам новой строки

# Подсчитать количество латинских букв
for char in content:
    if char.isalpha() and char.isascii():
        latin_letters_count += 1

# Вывести результаты статистики
print(f"Number of Latin letters: {latin_letters_count}")
print(f"Number of words: {word_count}")
print(f"Number of lines: {line_count}")
