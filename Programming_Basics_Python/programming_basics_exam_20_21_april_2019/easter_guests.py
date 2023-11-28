from math import ceil

number_of_guests = int(input())
budget = int(input())

needed_easter_bread = ceil(number_of_guests / 3)
eggs = number_of_guests * 2
easter_bread_price = needed_easter_bread * 4
eggs_price = eggs * 0.45

total_costs = easter_bread_price + eggs_price

if budget >= total_costs:
    print(f'Lyubo bought {needed_easter_bread} Easter bread and {eggs} eggs.\nHe has {budget - total_costs:.2f} lv. left.')
else:
    print(f'Lyubo doesn\'t have enough money.\nHe needs {total_costs - budget:.2f} lv. more.')
