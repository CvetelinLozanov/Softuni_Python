flat_number = int(input())
apartment_number = int(input())
flat_name = ''

for floor_number in range(flat_number, 0, -1):
    for apartment in range(apartment_number):

        if floor_number == flat_number:
            flat_name = f'L{floor_number}{apartment}'
        elif floor_number % 2 == 0:
            flat_name = f'O{floor_number}{apartment}'
        elif floor_number % 2 != 0:
            flat_name = f'A{floor_number}{apartment}'

        print(flat_name, end=' ')

    print()