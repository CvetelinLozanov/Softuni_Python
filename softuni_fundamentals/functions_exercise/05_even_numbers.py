from typing import List


def get_even_numbers(numbers: List[int]) -> List[int]:
    return list(filter(lambda n: n % 2 == 0, numbers))


numbers = [int(num) for num in input().split()]
print(get_even_numbers(numbers))