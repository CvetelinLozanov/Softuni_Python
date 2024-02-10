from typing import List


def get_positive_numbers(numbers: List[int]) -> List[int]:
    return list(filter(lambda n: n >= 0, numbers))


def get_negative_numbers(numbers: List[int]) -> List[int]:
    return list(filter(lambda n: n < 0, numbers))


def get_even_num(numbers: List[int]) -> List[int]:
    return list(filter(lambda n: n % 2 == 0, numbers))


def get_odd_nums(numbers: List[int]) -> List[int]:
    return list(filter(lambda n: n % 2 != 0, numbers))


def number_classification():
    numbers = [int(num) for num in input().split(', ')]
    positive_nums = get_positive_numbers(numbers)
    negative_nums = get_negative_numbers(numbers)
    even_nums = get_even_num(numbers)
    odd_nums = get_odd_nums(numbers)

    print(f'Positive: {", ".join(map(str, positive_nums))}')
    print(f'Negative: {", ".join(map(str, negative_nums))}')
    print(f'Even: {", ".join(map(str, even_nums))}')
    print(f'Odd: {", ".join(map(str, odd_nums))}')


number_classification()