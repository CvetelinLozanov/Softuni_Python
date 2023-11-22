type_of_screening = input()
number_of_rows = int(input())
number_of_columns = int(input())

price = 0
income = 0

if type_of_screening == 'Premiere':
    price = 12
elif type_of_screening == 'Normal':
    price = 7.5
elif type_of_screening == 'Discount':
    price = 5

income = number_of_columns * number_of_rows * price

print(f'{income:.2f} leva')