quantity_of_decorations = int(input())
days_till_christmas = int(input())

total_price = 0
total_points = 0

for day in range(1, days_till_christmas + 1):

    if day % 11 == 0:
        quantity_of_decorations += 2

    if day % 2 == 0:
        total_price += quantity_of_decorations * 2
        total_points += 5

    if day % 3 == 0:
        total_price += quantity_of_decorations * 5 + quantity_of_decorations * 3
        total_points += 13

    if day % 5 == 0:
        total_price += quantity_of_decorations * 15
        total_points += 17

    if day % 15 == 0:
        total_points += 30

    if day % 10 == 0:
        total_points -= 20
        total_price += 23

if days_till_christmas % 10 == 0:
    total_points -= 30

print(f'Total cost: {total_price}')
print(f'Total spirit: {total_points}')

