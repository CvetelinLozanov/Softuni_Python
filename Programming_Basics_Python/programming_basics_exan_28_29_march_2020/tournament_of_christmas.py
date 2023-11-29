days_of_tournaments = int(input())
funds_for_charity = 0

victories = 0
loses = 0
victory_days = 0
lose_days = 0
total_funds_for_charity = 0

for _ in range(days_of_tournaments):
    command = input()

    while command != 'Finish':
        possibilities = input()

        if possibilities == 'win':
            funds_for_charity += 20
            victories += 1

        elif possibilities == 'lose':
            loses += 1

        command = input()

    if victories > loses:
        funds_for_charity *= 1.10
        victory_days += 1
    else:
        lose_days += 1

    total_funds_for_charity += funds_for_charity
    victories = 0
    loses = 0
    funds_for_charity = 0

if victory_days > lose_days:
    total_funds_for_charity *= 1.20
    print(f'You won the tournament! Total raised money: {total_funds_for_charity:.2f}')

else:
    print(f'You lost the tournament! Total raised money: {total_funds_for_charity:.2f}')




