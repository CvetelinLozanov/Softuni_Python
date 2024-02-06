from typing import List


def swap_index_in_list(_index1:int, _index2: int, _numbers: List[int]):
    _numbers[_index1], _numbers[_index2] = numbers[_index2], _numbers[_index1]


def multiply_list_numbers_at_given_indexes(_index1: int, _index2: int, _numbers: List[int]):
    first_num, second_num = numbers[_index1], numbers[_index2]
    result = first_num * second_num
    numbers[_index1] = result


# Function to decrease value with one in list with numbers
def decrease_value_by_one(_numbers: List[int]):
    return [(num - 1) for num in _numbers]


numbers = list(map(int, input().split()))
command = input()

while True:
    if command == 'end':
        break

    command_args = command.split()

    if command_args[0] == 'swap':
        index1, index2 = command_args[1:]
        index1 = int(index1)
        index2 = int(index2)
        swap_index_in_list(index1, index2, numbers)

    elif command_args[0] == 'multiply':
        index1, index2 = command_args[1:]
        index1 = int(index1)
        index2 = int(index2)
        multiply_list_numbers_at_given_indexes(index1, index2, numbers)

    elif command_args[0] == 'decrease':
        numbers = decrease_value_by_one(numbers)

    command = input()

print(', '.join(map(str, numbers)))