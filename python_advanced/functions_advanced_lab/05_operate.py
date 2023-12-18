from functools import reduce

def operate(sign, *args):

    def add(args):
        return reduce(lambda a, b: a + b, args)
    def subtract(args):
        return reduce(lambda a, b: a - b, args)
    def multiply(args):
        return reduce(lambda a, b: a * b, args)
    def divide(args):
        return reduce(lambda a, b: a / b, args)

    mapper = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    return mapper[sign](args)

print(operate("+", 1, 2, 3))