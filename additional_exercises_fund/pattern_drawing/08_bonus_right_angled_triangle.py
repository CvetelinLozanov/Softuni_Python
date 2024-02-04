def print_triangle(n: int):
    for row in range(1, n + 1):
        print('*' * row)


n = int(input())
print_triangle(n)
