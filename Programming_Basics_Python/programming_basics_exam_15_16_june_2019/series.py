budget = float(input())
number_of_series = int(input())
total_costs = 0

for _ in range(number_of_series):
    series_name = input()
    price_for_series = float(input())

    if series_name == 'Thrones':
        price_for_series *= 0.50

    elif series_name == 'Lucifer':
        price_for_series *= 0.60

    elif series_name == 'Protector':
        price_for_series *= 0.70

    elif series_name == 'TotalDrama':
        price_for_series *= 0.80

    elif series_name == 'Area':
        price_for_series *= 0.90

    total_costs = price_for_series
    budget -= total_costs

if budget >= 0:
    print(f'You bought all the series and left with {budget:.2f} lv.')

else:
    print(f'You need {abs(budget):.2f} lv. more to buy the series!')