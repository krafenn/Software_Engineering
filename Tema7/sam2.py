def add_expense(amount, category, file):
    record = f"{amount} {category}\n"
    with open(file, 'a', encoding='utf-8') as expense_file:
        expense_file.write(record)
    print("Расход успешно записан!")

def show_expenses(file):
    try:
        with open(file, 'r') as expense_file:
            expenses = expense_file.readlines()
            if expenses:
                print("\nСуществующие расходы:")
                for expense in expenses:
                    print(expense.strip())
            else:
                print("\nНет сохраненных расходов.")
    except FileNotFoundError:
        print("\nФайл не найден или расходы не сохранены.")

expenses_file = "расходы.txt"

print("Программа учета расходов")
while True:
    print("\nВыберите действие:")
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Выйти")
    choice = input("Введите номер действия: ")

    if choice == "1":
        amount = input("Введите сумму расхода: ")
        category = input("Введите категорию расхода: ")
        add_expense(amount, category, expenses_file)
    elif choice == "2":
        show_expenses(expenses_file)
    elif choice == "3":
        print("До свидания!")
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")

