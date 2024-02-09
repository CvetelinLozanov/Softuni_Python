def even_numbers_indexes():
    numbers = list(map(int, input().split(', ')))
    even_numbers_indexes = [numbers.index(num, i) for i, num in enumerate(numbers) if num % 2 == 0]

    return even_numbers_indexes


print(even_numbers_indexes())
