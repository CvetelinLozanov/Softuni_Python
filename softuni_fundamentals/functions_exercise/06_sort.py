from typing import List


def sort_numbers(_numbers: List[int]) -> List[int]:
    return list(sorted(_numbers, key=lambda x: -x))


numbers = [int(num) for num in input().split()]
print(sort_numbers(numbers))