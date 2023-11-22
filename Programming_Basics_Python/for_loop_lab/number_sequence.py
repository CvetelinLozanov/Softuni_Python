from sys import maxsize

numbers = int(input())
max_number = -maxsize
min_number = maxsize

for num in range(numbers):
    input_number = int(input())

    if input_number > max_number:
        max_number = input_number

    if input_number < min_number:
        min_number = input_number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')