def sum_numbers(first_num: int, second_num: int) -> int:
    return first_num + second_num


def subtract(first_num: int, second_num: int) -> int:
    return first_num - second_num


def add_and_subtract(first_num: int, second_num: int, third_num: int) -> int:
    result_from_sum = sum_numbers(first_num, second_num)
    result_from_subtraction = subtract(result_from_sum, third_num)
    return result_from_subtraction


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))