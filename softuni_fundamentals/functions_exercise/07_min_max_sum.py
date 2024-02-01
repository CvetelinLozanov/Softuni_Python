from typing import List


def get_min_max_and_sum(numbers: List[int]) -> str:
    min_num = get_min_number(numbers)
    max_num = get_max_number(numbers)
    sum_of_numbers = get_sum_of_numbers(numbers)
    return (f'The minimum number is {min_num}\n'
            f'The maximum number is {max_num}\n'
            f'The sum number is: {sum_of_numbers}')


def get_min_number(numbers: List[int]):
    return min(numbers)


def get_max_number(numbers: List[int]):
    return max(numbers)


def get_sum_of_numbers(numbers: List[int]):
    return sum(numbers)


numbers = [int(num) for num in input().split()]
print(get_min_max_and_sum(numbers))