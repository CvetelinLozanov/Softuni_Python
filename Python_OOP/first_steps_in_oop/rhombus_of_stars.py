def first_triangle(n):
    for row in range(1, n + 1):
        print_triangle(n, row)


def second_triangle(n):
    for row in range(n - 1, 0, -1):
        print_triangle(n, row)


def print_triangle(n, row):
    print(' ' * (n - row), end='')
    print(*['*'] * row)


def rhombus_of_stars(n):
    first_triangle(n)
    second_triangle(n)


n = int(input())
rhombus_of_stars(n)