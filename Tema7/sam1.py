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
