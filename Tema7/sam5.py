file_name = 'text.txt'

try:
    with open(file_name, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        print(f"Количество слов в файле '{file_name}': {word_count}")

except FileNotFoundError:
    print(f"Файл '{file_name}' не найден")
