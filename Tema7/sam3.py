with open('inputsam2.txt', 'r') as file:
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
