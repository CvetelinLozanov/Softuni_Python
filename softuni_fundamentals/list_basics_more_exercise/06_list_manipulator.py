def is_valid_index(index, list):
    return 0 <= index < len(list)


numbers = [int(num) for num in input().split()]

while True:
    text = input()

    if text == 'end':
        break

    command_args = text.split()
    command = command_args[0]

    if command == 'exchange':
        index = int(command_args[1])

        if not is_valid_index(index, numbers):
            print('Invalid index')
            continue

        first_list = numbers[:index + 1]
        second_list = numbers[index + 1:]

        numbers = second_list + first_list

    elif command == 'max':
        sub_command = command_args[1]

        if sub_command == 'even':
            biggest_even_num = [num for num in numbers if num % 2 == 0]

            if not biggest_even_num:
                print('No matches')
                continue

            biggest_even_num = max(biggest_even_num)
            number_last_index = len(numbers) - 1 - numbers[::-1].index(biggest_even_num)
            print(number_last_index)

        if sub_command == 'odd':
            biggest_odd_num = [num for num in numbers if num % 2 != 0]

            if not biggest_odd_num:
                print('No matches')
                continue

            biggest_odd_num = max(biggest_odd_num)
            number_last_index = len(numbers) - 1 - numbers[::-1].index(biggest_odd_num)
            print(number_last_index)

    elif command == 'min':
        sub_command = command_args[1]

        if sub_command == 'even':
            smallest_even_num = [num for num in numbers if num % 2 == 0]

            if not smallest_even_num:
                print('No matches')
                continue

            smallest_even_num = min(smallest_even_num)
            number_last_index = len(numbers) - 1 - numbers[::-1].index(smallest_even_num)
            print(number_last_index)

        if sub_command == 'odd':
            smallest_odd_num = [num for num in numbers if num % 2 != 0]

            if not smallest_odd_num:
                print('No matches')
                continue

            smallest_odd_num = min(smallest_odd_num)
            number_last_index = len(numbers) - 1 - numbers[::-1].index(smallest_odd_num)
            print(number_last_index)

    elif command == 'first':
        count = int(command_args[1])
        sub_command = command_args[2]
        even_nums = []
        odd_nums = []

        if count > len(numbers):
            print('Invalid count')
            continue

        if sub_command == 'even':
            even_nums = [num for num in numbers if num % 2 == 0]
            # if len(even_nums) < count:
            #     count = len(even_nums)
            final_nums = even_nums[:count]
            print(final_nums)

        elif sub_command == 'odd':
            odd_nums = [num for num in numbers if num % 2 != 0]
            # if len(odd_nums) < count:
            #     count = len(odd_nums)
            final_nums = odd_nums[:count]
            print(final_nums)

    elif command == 'last':
        count = int(command_args[1])
        sub_command = command_args[2]
        even_nums = []
        odd_nums = []

        if count > len(numbers):
            print('Invalid count')
            continue

        if sub_command == 'even':
            even_nums = [num for num in numbers if num % 2 == 0]
            # if len(even_nums) < count:
            #     count = len(even_nums)
            final_nums = even_nums[-count:]
            print(final_nums)

        elif sub_command == 'odd':
            odd_nums = [num for num in numbers if num % 2 != 0]
            # if len(odd_nums) < count:
            #     count = len(odd_nums)
            final_nums = odd_nums[-count:]
            print(final_nums)

print(numbers)