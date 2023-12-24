from modules.mathematical_operations.core.operations import add, subtract, divide, pow, multiply

operations_mapper = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '^': pow
}


def calculation(num1, sign, num2):
    return f'{operations_mapper[sign](num1, num2):.2f}'
