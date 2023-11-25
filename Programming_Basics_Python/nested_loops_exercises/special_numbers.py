number = int(input())
counter = 0

for num in range(1111, 10000):
    number_to_string = str(num)
    for index, digit in enumerate(number_to_string):
        if int(digit) == 0:
            break
        if number % int(digit) == 0:
            counter += 1

    if counter == 4:
        print(num, end=' ')
    counter = 0
