month = input()
number_of_nights = int(input())

studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    studio_price = 50 * number_of_nights
    apartment_price = 65 * number_of_nights
    if 7 < number_of_nights < 14:
        studio_price *= 0.95
    elif number_of_nights > 14:
        studio_price *= 0.70
        apartment_price *= 0.90
elif month == 'June' or month == 'September':
    studio_price = 75.20 * number_of_nights
    apartment_price = 68.70 * number_of_nights
    if number_of_nights > 14:
        studio_price *= 0.80
        apartment_price *= 0.90
elif month == 'July' or month == 'August':
    studio_price = 76 * number_of_nights
    apartment_price = 77 * number_of_nights
    if number_of_nights > 14:
        apartment_price *= 0.90

print(f'Apartment: {apartment_price:.2f} lv.\n'
      f'Studio: {studio_price:.2f} lv.')