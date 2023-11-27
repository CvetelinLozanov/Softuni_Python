budget = float(input())
number_of_stats = int(input())
price_for_wear = float(input())

decor = budget * 0.10

total_price_for_clothes = price_for_wear * number_of_stats

if number_of_stats > 150:
    total_price_for_clothes *= 0.90

total_costs = decor + total_price_for_clothes

if total_costs > budget:
    print(f'Not enough money!\nWingard needs {total_costs - budget:.2f} leva more.')
else:
    print(f'Action!\nWingard starts filming with {budget - total_costs:.2f} leva left.')