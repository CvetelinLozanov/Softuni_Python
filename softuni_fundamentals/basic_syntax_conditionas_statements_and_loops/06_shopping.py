budget = int(input())

while True:
    command = input()

    if command == 'End':
        print('You bought everything needed.')
        break

    cost = int(command)

    budget -= cost

    if budget < 0:
        print('You went in overdraft!')
        break

