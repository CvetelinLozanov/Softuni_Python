coffee_counter = 0
is_end = False

while True:
    command = input()

    if command == 'END':
        break

    if command in ['coding', 'dog', 'cat', 'movie']:
        coffee_counter += 1

    elif command in ['CODING', 'CAT', 'DOG', 'MOVIE']:
        coffee_counter += 2

    if coffee_counter > 5:
        print('You need extra sleep')
        is_end = True
        break

if not is_end:
    print(coffee_counter)

