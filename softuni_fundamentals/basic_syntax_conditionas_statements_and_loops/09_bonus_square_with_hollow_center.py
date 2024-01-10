def print_stars(n: int):
    print('*' * n)


def print_middle_part(n: int):
    for _ in range(n - 2):
        print('*', end='')
        print(' ' * (n - 2), end='')
        print('*')


n = int(input())
print_stars(n)
print_middle_part(n)
print_stars(n)