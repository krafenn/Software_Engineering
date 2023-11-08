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
