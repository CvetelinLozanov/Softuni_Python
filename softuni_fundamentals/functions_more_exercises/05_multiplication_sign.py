def multiplication_sign(numbers):
    if 0 in numbers:
        return 'zero'

    filtered_numbers = list(filter(lambda number: number < 0, numbers))
    if len(filtered_numbers) % 2 != 0:
        return 'negative'

    return 'positive'


numbers = [int(input()) for _ in range(3)]
print(multiplication_sign(numbers))
