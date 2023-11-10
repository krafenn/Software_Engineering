def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            if not data:
                raise Exception("Файл пустой")
            else:
                print("Информация из файла:")
                print(data)
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print(e)

empty_file_path = "empty_file.txt"
with open(empty_file_path, 'w'):
    pass

non_empty_file_path = "non_empty_file.txt"
with open(non_empty_file_path, 'w') as file:
    file.write("info")

read_file(empty_file_path)
read_file(non_empty_file_path)