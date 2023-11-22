first_number = int(input())
second_number = int(input())
input_operator = input()

if input_operator == '+':
    result = first_number + second_number
    if result % 2 == 0:
        print(f'{first_number} {input_operator} {second_number} = {result} - even')
    else:
        print(f'{first_number} {input_operator} {second_number} = {result} - odd')
elif input_operator == '-':
    result = first_number - second_number
    if result % 2 == 0:
        print(f'{first_number} {input_operator} {second_number} = {result} - even')
    else:
        print(f'{first_number} {input_operator} {second_number} = {result} - odd')
elif input_operator == '*':
    result = first_number * second_number
    if result % 2 == 0:
        print(f'{first_number} {input_operator} {second_number} = {result} - even')
    else:
        print(f'{first_number} {input_operator} {second_number} = {result} - odd')
elif input_operator == '/':
    if second_number == 0:
        print(f'Cannot divide {first_number} by zero')
    else:
        result = first_number / second_number
        print(f'{first_number} / {second_number} = {result:.2f}')
elif input_operator == '%':
    if second_number == 0:
        print(f'Cannot divide {first_number} by zero')
    else:
        result = first_number % second_number
        print(f'{first_number} % {second_number} = {result}')