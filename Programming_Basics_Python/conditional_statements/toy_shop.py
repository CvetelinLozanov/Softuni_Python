puzzle = 2.6
speaking_doll = 3
fluffy_bear = 4.1
minion = 8.2
truck = 2

price_for_trip = float(input())
number_of_puzzles = int(input())
number_of_speaking_dolls = int(input())
number_of_fluffy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

puzzle_costs = puzzle * number_of_puzzles
speaking_dolls_costs = number_of_speaking_dolls * speaking_doll
fluffy_bear_costs = number_of_fluffy_bears * fluffy_bear
minion_costs = number_of_minions * minion
trucks_costs = truck * number_of_trucks
total_income = puzzle_costs + speaking_dolls_costs + fluffy_bear_costs + minion_costs + trucks_costs
count_of_ordered_toys = number_of_minions + number_of_trucks + number_of_puzzles + number_of_fluffy_bears + number_of_speaking_dolls

if count_of_ordered_toys >= 50:
    total_income *= 0.75

total_income *= 0.9

if total_income >= price_for_trip:
    print(f'Yes! {total_income - price_for_trip:.2f} lv left.')
else:
    print(f'Not enough money! {price_for_trip - total_income:.2f} lv needed.')