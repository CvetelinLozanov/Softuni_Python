def print_upper_part(n):
    for row in range(1, n + 1):
        print_stars(row)


def print_lower_part(n):
    for row in range(n - 1, 0, -1):
        print_stars(row)


def print_stars(row):
    print('*' * row)


def print_triangle(n):
    print_upper_part(n)
    print_lower_part(n)


n = int(input())
print_triangle(n)

