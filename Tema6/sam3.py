def count_most_frequent_numbers(numbers):
    count_dict = {}
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    sorted_dict = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))
    most_frequent = dict(list(sorted_dict.items())[:3])

    return dict(sorted(most_frequent.items()))

random_sequence = "793727573817264"

if len(random_sequence) >= 15:
    result = count_most_frequent_numbers(random_sequence)
    print("Словарь из 3 наиболее часто встречающихся чисел:")
    print(result)
else:
    print("Последовательность должна содержать минимум 15 символов.")
