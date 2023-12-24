def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    try:
        num1 / num2
        return num1 / num2
    except ZeroDivisionError:
        print('Cannot divide with 0')
        return 0


def multiply(num1, num2):
    return num1 * num2


def pow(num1, num2):
    return num1 ** num2
