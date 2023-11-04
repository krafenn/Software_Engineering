import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

max_values = [max(one), max(two), max(three)]
min_values = [min(one), min(two), min(three)]

areas = []

for values in [max_values, min_values]:
    a, b, c = sorted(values)
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    areas.append(area)

max_area, min_area = areas

print(f"Площадь треугольника с максимальными сторонами: {max_area}")
print(f"Площадь треугольника с минимальными сторонами: {min_area}")
