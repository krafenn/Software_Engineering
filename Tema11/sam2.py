def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 200
fibonacci_sequence = list(fib(n))

with open("fib.txt", "w") as file:
    for number in fibonacci_sequence:
        file.write(str(number) + "\n")

print(f"Число Фибоначчи от {n}: {fibonacci_sequence[-1]}")
