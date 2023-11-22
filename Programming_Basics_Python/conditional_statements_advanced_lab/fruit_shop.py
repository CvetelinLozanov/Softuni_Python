def price_for_working_days(product):
    price = 0

    if product == 'banana':
        price = 2.50
    elif product == 'apple':
        price = 1.20
    elif product == 'orange':
        price = 0.85
    elif product == 'grapefruit':
        price = 1.45
    elif product == 'kiwi':
        price = 2.70
    elif product == 'pineapple':
        price = 5.50
    elif product == 'grapes':
        price = 3.85

    return price

def price_for_weekend(product):
    price = 0

    if product == 'banana':
        price = 2.70
    elif product == 'apple':
        price = 1.25
    elif product == 'orange':
        price = 0.90
    elif product == 'grapefruit':
        price = 1.60
    elif product == 'kiwi':
        price = 3
    elif product == 'pineapple':
        price = 5.60
    elif product == 'grapes':
        price = 4.20

    return price

product = input()
day_of_week = input()
quantity = float(input())

price = 0

if day_of_week == 'Monday':
    price = price_for_working_days(product)
elif day_of_week == 'Tuesday':
    price = price_for_working_days(product)
elif day_of_week == 'Wednesday':
    price = price_for_working_days(product)
elif day_of_week == 'Thursday':
    price = price_for_working_days(product)
elif day_of_week == 'Friday':
    price = price_for_working_days(product)
elif day_of_week == 'Saturday':
    price = price_for_weekend(product)
elif day_of_week == 'Sunday':
    price = price_for_weekend(product)

if not price == 0:
    print(f'{quantity * price:.2f}')
else:
    print('error')