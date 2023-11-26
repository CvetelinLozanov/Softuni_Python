type_of_championship = input()
type_of_ticket = input()
number_of_tickets = int(input())
picture_with_trophy = input()

total_price_for_tickets = 0

if type_of_championship == 'Quarter final':
    if type_of_ticket == 'Standard':
        total_price_for_tickets = number_of_tickets * 55.5
    elif type_of_ticket == 'Premium':
        total_price_for_tickets = number_of_tickets * 105.2
    elif type_of_ticket == 'VIP':
        total_price_for_tickets = number_of_tickets * 118.9

elif type_of_championship == 'Semi final':
    if type_of_ticket == 'Standard':
        total_price_for_tickets = number_of_tickets * 75.88
    elif type_of_ticket == 'Premium':
        total_price_for_tickets = number_of_tickets * 125.22
    elif type_of_ticket == 'VIP':
        total_price_for_tickets = number_of_tickets * 300.4

elif type_of_championship == 'Final':
    if type_of_ticket == 'Standard':
        total_price_for_tickets = number_of_tickets * 110.10
    elif type_of_ticket == 'Premium':
        total_price_for_tickets = number_of_tickets * 160.66
    elif type_of_ticket == 'VIP':
        total_price_for_tickets = number_of_tickets * 400


if total_price_for_tickets > 4000:
        total_price_for_tickets *= 0.75

elif total_price_for_tickets > 2500:

    if picture_with_trophy == 'Y':
        total_price_for_tickets = (total_price_for_tickets * 0.9) + (40 * number_of_tickets)
    else:
        total_price_for_tickets *= 0.9
else:

    if picture_with_trophy == 'Y':
        total_price_for_tickets += 40 * number_of_tickets


print(f'{total_price_for_tickets:.2f}')
