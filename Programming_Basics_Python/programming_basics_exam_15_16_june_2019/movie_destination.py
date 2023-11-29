budget = float(input())
destination = input()
season = input()
number_of_days = int(input())
is_discount = False
discount = 0

price = 0

if destination == 'Dubai':

    is_discount = True
    discount = 0.70
    if season == 'Winter':
        price = 45000

    elif season == 'Summer':
        price = 40000

elif destination == 'Sofia':

    is_discount = True
    discount = 1.25

    if season == 'Winter':
        price = 17000

    elif season == 'Summer':
        price = 12500

elif destination == 'London':

    if season == 'Winter':
        price = 24000

    elif season == 'Summer':
        price = 20250

total_costs = price * number_of_days

if is_discount:
    total_costs *= discount

if budget >= total_costs:
    print(f'The budget for the movie is enough! We have {budget - total_costs:.2f} leva left!')

else:
    print(f'The director needs {total_costs - budget:.2f} leva more!')