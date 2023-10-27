from sam5 import main

a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

x = main(a, b, c)

print(f"Площадь треугольника: {x}")
