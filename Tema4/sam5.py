def main(a, b, c):
    s = (a + b + c) / 2

    x = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return x