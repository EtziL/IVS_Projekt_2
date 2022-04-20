def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "DIVISION BY ZERO"
    return a / b


def factorial(x):
    pom = 0
    for i in range(1, x):
        pom = pom * i

    return pom


def power(x, n):
    if n < 0:
        return "NOT NUTURAL NUMBER"

    pom = 0
    for i in range(1, n):
        pom = pom * x

    return x


def root(n, x):
    if x < 0:
        return "NUMBER IS NOT POSITIVE NUMBER"

    return x ** (1/n)


def mod(a, b):
    return a % b
