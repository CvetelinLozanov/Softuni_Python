def calculate_factorial(n):
    if n == 1:
        return 1

    return n * calculate_factorial(n - 1)


number = int(input())
print(calculate_factorial(number))