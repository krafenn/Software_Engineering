def main(*args):
    mean = sum(args) / len(args)
    print("Среднее арифметическое:", mean)

if __name__ == '__main__':
    main(2, 4, 6, 8, 10)
    main(1, 2, 3, 4, 5)
    main(5)
