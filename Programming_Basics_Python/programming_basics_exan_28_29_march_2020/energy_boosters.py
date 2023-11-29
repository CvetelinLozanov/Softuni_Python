fruit = input()
set_size = input()
number_of_sets = int(input())
price_for_set = 0

if fruit == 'Watermelon':
    if set_size == 'small':
        price_for_set = 2 * 56

    elif set_size == 'big':
        price_for_set = 5 * 28.70

elif fruit == 'Mango':
    if set_size == 'small':
        price_for_set = 2 * 36.66

    elif set_size == 'big':
        price_for_set = 5 * 19.60

elif fruit == 'Pineapple':
    if set_size == 'small':
        price_for_set = 2 * 42.10

    elif set_size == 'big':
        price_for_set = 5 * 24.80

elif fruit == 'Raspberry':
    if set_size == 'small':
        price_for_set = 2 * 20

    elif set_size == 'big':
        price_for_set = 5 * 15.20

total_costs = price_for_set * number_of_sets

if 400 <= total_costs <= 1000:
    total_costs *= 0.85

elif total_costs > 1000:
    total_costs *= 0.50


print(f'{total_costs:.2f} lv.')