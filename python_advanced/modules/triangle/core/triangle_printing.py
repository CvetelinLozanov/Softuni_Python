def print_numbers(line):
    for num in range(1, line + 1):
        print(num, end=' ')

def print_upper_part(n):
    for line in range(1, n + 1):
        print_numbers(line)
        print()

def print_bottom_part(n):
    for line in range(n - 1, 0, -1):
        print_numbers(line)
        print()


def print_triangle(n):
    print_upper_part(n)
    print_bottom_part(n)