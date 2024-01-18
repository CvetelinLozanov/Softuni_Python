lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
shield_broken_times = 0

for lose in range(1, lost_fights_count + 1):

    if lose % 2 == 0:
        expenses += helmet_price

    if lose % 3 == 0:
        expenses += sword_price
        if lose % 2 == 0:
            expenses += shield_price
            shield_broken_times += 1
            if shield_broken_times % 2 == 0:
                expenses += armor_price

print(f'Gladiator expenses: {expenses:.2f} aureus')