sentences = ["The car drove off the road at the end.", "The cat chased the mouse.", "His shirt was ugly."]

for i, sentence in enumerate(sentences, start=1):
    original_sentence = sentence

    sentence = sentence.lower()
    print(f"Предложение {i}: {original_sentence}")
    print(f"Длина предложения: {len(sentence)} символов")

    vowels_count = sum(1 for char in sentence if char in 'aeiou')
    print(f"Количество гласных в предложении: {vowels_count}")

    replaced_sentence = sentence.replace("ugly", "beauty")
    print(f"Предложение после замены: {replaced_sentence}")

    if sentence.startswith("the"):
        print("Предложение начинается с 'The'")
    else:
        print("Предложение не начинается с 'The'")

    if sentence.endswith("end"):
        print("Предложение заканчивается на 'end'")
    else:
        print("Предложение не заканчивается на 'end'")

    if i < len(sentences):
        print("-" * 30)