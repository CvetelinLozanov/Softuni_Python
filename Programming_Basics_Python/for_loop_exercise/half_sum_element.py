from sys import maxsize

numbers = int(input())

biggest_number = -maxsize
total_sum = 0

for num in range(numbers):
    input_number = int(input())
    if input_number > biggest_number:
        biggest_number = input_number

    total_sum += input_number

is_diff = abs(biggest_number - abs((biggest_number - total_sum)))

if is_diff == 0:
    print(f'Yes\nSum = {biggest_number}')
else:
    print(f'No\nDiff = {is_diff}')
