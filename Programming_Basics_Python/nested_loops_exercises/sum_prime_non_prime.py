sum_of_prime = 0
sum_of_non_prime = 0
dividing_counter = 0

while True:
    command = input()

    if command == 'stop':
        break

    number = int(command)

    if number < 0:
        print('Number is negative.')
        continue

    if number == 1:
        sum_of_non_prime += 1
        continue

    if number == 0:
        continue

    for num in range(2, number + 1):
        if number % num == 0:
            dividing_counter += 1

    if dividing_counter == 1:
        sum_of_prime += number
    else:
        sum_of_non_prime += number

    dividing_counter = 0

print(f'Sum of all prime numbers is: {sum_of_prime}')
print(f'Sum of all non prime numbers is: {sum_of_non_prime}')