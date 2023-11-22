from math import fabs


def get_price_for_boat_loan(season):

    price_for_loan = 0

    if season == 'Spring':
        price_for_loan = 3000
    elif season == 'Summer' or season == 'Autumn':
        price_for_loan = 4200
    elif season == 'Winter':
        price_for_loan = 2600

    return price_for_loan


def get_discount(number_of_fishers, price_for_loan):

    if 0 < number_of_fishers <= 6:
        price_for_loan *= 0.90
    elif 7 < number_of_fishers <= 11:
        price_for_loan *= 0.85
    elif number_of_fishers > 12:
        price_for_loan *= 0.75

    return price_for_loan


def check_if_number_is_even_or_odd(number_of_fishers):
    return number_of_fishers % 2 == 0


budget = int(input())
season = input()
number_of_fishers = int(input())

price_for_loan = get_price_for_boat_loan(season)
price_for_loan = get_discount(number_of_fishers, price_for_loan)

if check_if_number_is_even_or_odd(number_of_fishers):
    if not season == 'Autumn':
        price_for_loan *= 0.95

if budget >= price_for_loan:
    print(f'Yes! You have {budget - price_for_loan:.2f} leva left.')
else:
    print(f'Not enough money! You need {fabs(price_for_loan - budget):.2f} leva.')