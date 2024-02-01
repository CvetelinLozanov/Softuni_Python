from functools import reduce


def multiply(a, b):
    return reduce(lambda a, b: a * b, [a, b])


def divide(a, b):
    return reduce(lambda a, b: int(a / b), [a, b])


def add(a, b):
    return reduce(lambda a, b: a + b, [a, b])


def subtract(a, b):
    return reduce(lambda a, b: a - b, [a, b])


mapper = {
    'subtract': subtract,
    'multiply': multiply,
    'add': add,
    'divide': divide
}

operator = input()
first_num = int(input())
second_num = int(input())

print(mapper[operator](first_num, second_num))