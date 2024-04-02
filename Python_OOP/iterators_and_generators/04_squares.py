def squares(number: int):
    start = 1

    while start <= number:
        yield start ** 2
        start += 1


print(list(squares(5)))