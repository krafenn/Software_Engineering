from collections import defaultdict

def sets(input_list):
    num_counts = defaultdict(int)
    for num in input_list:
        num_counts[num] += 1

    result_set = set()
    for num, count in num_counts.items():
        if count == 1:
            result_set.add(num)
        else:
            result_set.update(str(num) * i for i in range(1, count + 1))

    return result_set

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

result_1 = sets(list_1)
result_2 = sets(list_2)
result_3 = sets(list_3)

print(result_1)
print(result_2)
print(result_3)
