eggs_stocks = int(input())

eggs_sold = 0

command = input()
while command != 'Close':

    number_of_eggs = int(input())

    if command == 'Fill':
        eggs_stocks += number_of_eggs

    elif command == 'Buy':

        if number_of_eggs > eggs_stocks:
            print(f'Not enough eggs in store!')
            print(f'You can buy only {eggs_stocks}.')
            break
        else:
            eggs_stocks -= number_of_eggs
            eggs_sold += number_of_eggs

    command = input()

else:
    print(f'Store is closed!')
    print(f'{eggs_sold} eggs sold.')