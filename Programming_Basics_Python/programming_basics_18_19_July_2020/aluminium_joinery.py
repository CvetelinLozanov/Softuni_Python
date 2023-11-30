number_of_joinery = int(input())
type_of_joinery = input()
delivery = input()
price_for_joinery = 0


if number_of_joinery <= 10:
    print('Invalid order')
    exit()

elif type_of_joinery == '90X130':
    price_for_joinery = number_of_joinery * 110

    if 30 < number_of_joinery < 60:
        price_for_joinery *= 0.95

    elif number_of_joinery > 60:
        price_for_joinery *= 0.92


elif type_of_joinery == '100X150':
    price_for_joinery = number_of_joinery * 140

    if 40 < number_of_joinery < 80:
        price_for_joinery *= 0.94

    elif number_of_joinery > 80:
        price_for_joinery *= 0.90

elif type_of_joinery == '130X180':
    price_for_joinery = number_of_joinery * 190

    if 20 < number_of_joinery < 50:
        price_for_joinery *= 0.93

    elif number_of_joinery > 50:
        price_for_joinery *= 0.88

elif type_of_joinery == '200X300':
    price_for_joinery = number_of_joinery * 250

    if 25 < number_of_joinery < 50:
        price_for_joinery *= 0.91

    elif number_of_joinery > 50:
        price_for_joinery *= 0.86

if delivery == 'With delivery':
    price_for_joinery += 60

if number_of_joinery > 99:
    price_for_joinery *= 0.96

print(f'{price_for_joinery:.2f} BGN')