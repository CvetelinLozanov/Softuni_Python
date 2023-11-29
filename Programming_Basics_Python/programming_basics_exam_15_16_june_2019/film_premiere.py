movie = input()
packet_for_movie = input()
tickets_number = int(input())
discount = 0
is_discount = False

ticket_price = 0

if movie == 'John Wick':

    if packet_for_movie == 'Drink':
        ticket_price = 12

    elif packet_for_movie == 'Popcorn':
        ticket_price = 15

    elif packet_for_movie == 'Menu':
        ticket_price = 19

elif movie == 'Star Wars':

    if packet_for_movie == 'Drink':
        ticket_price = 18

    elif packet_for_movie == 'Popcorn':
        ticket_price = 25

    elif packet_for_movie == 'Menu':
        ticket_price = 30

    if tickets_number >= 4:
        discount = 0.70
        is_discount = True

elif movie == 'Jumanji':

    if packet_for_movie == 'Drink':
        ticket_price = 9

    elif packet_for_movie == 'Popcorn':
        ticket_price = 11

    elif packet_for_movie == 'Menu':
        ticket_price = 14

    if tickets_number == 2:
        discount = 0.85
        is_discount = True

total_price_to_pay = tickets_number * ticket_price

if is_discount:
    total_price_to_pay *= discount

print(f'Your bill is {total_price_to_pay:.2f} leva.')