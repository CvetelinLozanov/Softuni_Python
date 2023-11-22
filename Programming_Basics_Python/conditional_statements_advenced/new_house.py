from math import fabs


def get_price_for_flower(type_of_flower):

    price = 0

    if type_of_flower == 'Roses':
        price = 5
    elif type_of_flower == 'Dahlias':
        price = 3.80
    elif type_of_flower == 'Tulips':
        price = 2.80
    elif type_of_flower == 'Narcissus':
        price = 3
    elif type_of_flower == 'Gladiolus':
        price = 2.50

    return price


def get_total_costs(price, number_of_flowers):
    total_costs = price * number_of_flowers
    return total_costs


def get_discount_or_appreciation(type_of_flower, total_costs, number_of_flowers):
    if type_of_flower == 'Roses':
        if number_of_flowers > 80:
            total_costs *= 0.90
    elif type_of_flower == 'Dahlias':
        if number_of_flowers > 90:
            total_costs *= 0.85
    elif type_of_flower == 'Tulips':
        if number_of_flowers > 80:
            total_costs *= 0.85
    elif type_of_flower == 'Narcissus':
        if number_of_flowers < 120:
            total_costs *= 1.15
    elif type_of_flower == 'Gladiolus':
        if number_of_flowers < 80:
            total_costs *= 1.20

    return total_costs


type_of_flower = input()
number_of_flowers = int(input())
budget = int(input())

price_for_flower = get_price_for_flower(type_of_flower)
total_costs = get_total_costs(price_for_flower, number_of_flowers)
final_costs = get_discount_or_appreciation(type_of_flower, total_costs, number_of_flowers)

if final_costs <= budget:
    remaining_money = budget - final_costs
    print(f'Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {remaining_money:.2f} leva left.')
else:
    not_enough_money = budget - final_costs
    print(f'Not enough money, you need {fabs(not_enough_money):.2f} leva more.')
