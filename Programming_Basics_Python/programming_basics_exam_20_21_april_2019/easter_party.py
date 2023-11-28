number_of_guests = int(input())
tax = float(input())
budget = float(input())

cake_price = budget * 0.10

if 10 <= number_of_guests <= 15:
    tax *= 0.85

elif 15 < number_of_guests <= 20:
    tax *= 0.80

elif number_of_guests > 20:
    tax *= 0.75

tax_for_guests = tax * number_of_guests
total_price_to_pay = tax_for_guests + cake_price

if budget >= total_price_to_pay:
    print(f'It is party time! {budget - total_price_to_pay:.2f} leva left.')
else:
    print(f'No party! {total_price_to_pay - budget:.2f} leva needed.')