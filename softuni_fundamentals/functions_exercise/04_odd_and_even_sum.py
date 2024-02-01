from typing import List


def sum_odd_and_even_numbers(number: List[str]) -> str:
    even_sum = sum(sum_even_numbers(number))
    odd_sum = sum(sum_odd_numbers(number))
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


def sum_even_numbers(number: List[str]) -> List[int]:
    return [int(num) for num in number if int(num) % 2 == 0]


def sum_odd_numbers(number: List[str]) -> List[int]:
    return [int(num) for num in number if int(num) % 2 != 0]


num_as_string = list(input())
print(sum_odd_and_even_numbers(num_as_string))