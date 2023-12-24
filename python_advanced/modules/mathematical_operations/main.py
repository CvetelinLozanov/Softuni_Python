from modules.mathematical_operations.core.executor import calculation

num1, sign, num2, = input().split()

print(calculation(float(num1), sign, float(num2)))