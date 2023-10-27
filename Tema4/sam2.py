import random

def main():
    x = random.randint(1, 6)
    print("Кубик:", x)

    if x == 5 or x == 6:
        print("Вы победили")
    elif x == 3 or x == 4:
        print("Попробуйте еще раз:")
        main()
    else:
        print("Вы проиграли")

if __name__ == "__main__":
    main()
