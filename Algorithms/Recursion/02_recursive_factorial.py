def calculate_factorial(num):
    if num <= 1:
        return 1

    return num * calculate_factorial(num - 1)


num = int(input())
print(calculate_factorial(num))