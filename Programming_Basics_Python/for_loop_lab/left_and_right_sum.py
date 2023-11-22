number = int(input())

first_sum = 0
second_sum = 0

for num in range(number):
    input_number = int(input())
    first_sum += input_number

for num in range(number):
    input_number = int(input())
    second_sum += input_number

if first_sum == second_sum:
    print(f'Yes, sum = {first_sum}')
else:
    print(f'No, diff = {abs(first_sum - second_sum)}')
