# def first_triangle(n: int):
#     for row in range(n // 2):
#         print(' ' * (n // 2 - row), end='')
#         print('*' * (row + row + 1), end='')
#         print(' ' * (n // 2 - row))
#
#
# def second_triangle(n: int):
#     for row in range(n // 2, -1, -1):
#         print(' ' * (n // 2 - row), end='')
#         print('*' * (row + row + 1), end='')
#         print(' ' * (n // 2 - row))


def first_triangle(n: int):
    for row in range(n // 2 + 1):
        print_symbols(row)


def second_triangle(n: int):
    for row in range(n // 2 - 1, -1, -1):
        print_symbols(row)


def print_symbols(times: int):
    print(' ' * (n // 2 - times), end='')
    print('*' * (times + times + 1), end='')
    print(' ' * (n // 2 - times))


def diamond(n):
    first_triangle(n)
    second_triangle(n)


n = int(input())

diamond(n)
