input_data = input("Введите последовательность чисел, разделенных пробелом: ")

numbers_list = list(map(int, input_data.split()))
numbers_tuple = tuple(numbers_list)

print("Список чисел:", numbers_list)
print("Кортеж чисел:", numbers_tuple)
