beginning_of_interval = int(input())
end_of_interval = int(input())
magic_number = int(input())
combination_counter = 0
is_combination = False

result_string = ''

for num1 in range(beginning_of_interval, end_of_interval + 1):
    for num2 in range(beginning_of_interval, end_of_interval + 1):
        combination_counter += 1

        if num1 + num2 == magic_number:
            result_string = f'Combination N:{combination_counter} ({num1} + {num2} = {magic_number})'
            is_combination = True
            break

    if is_combination:
        break

if not is_combination:
    print(f'{combination_counter} combinations - neither equals {magic_number}')
else:
    print(result_string)

