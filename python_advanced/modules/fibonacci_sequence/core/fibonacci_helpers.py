def create_fibonacci_sequence(n):
    fibonacci_numbers = [0, 1]
    for _ in range(n - 2):
        first_num = fibonacci_numbers[-2]
        second_num = fibonacci_numbers[-1]

        fibonacci_numbers.append(first_num + second_num)

    return fibonacci_numbers


def print_numbers(numbers):
    print(*numbers)


def locate_number(searched_number, fibonacci_numbers):
    try:
        index = fibonacci_numbers.index(searched_number)
        return f'The number - {searched_number} is at index {index}'
    except ValueError:
        return f'The number {searched_number} is not in the sequence'
