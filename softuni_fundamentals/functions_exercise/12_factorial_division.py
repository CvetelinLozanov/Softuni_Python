# def factorial_recursion(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial_recursion(n - 1)


# def calculate_factorial(number: int):
#     factorial_num = 1
#     for num in range(2, number + 1):
#         factorial_num *= num
#
#     return factorial_num
#
#
# num = int(input())
# divisor = int(input())
# factorial_number = calculate_factorial(num)
# print(f'{factorial_number / divisor:.2f}')


import math


num = int(input())
divisor = int(input())

print(f'{math.factorial(num) / divisor:.2f}')
