destination = input()
savings = 0.0

while destination != 'End':
    needed_budget = float(input())
    while savings < needed_budget:
        income = float(input())
        savings += income

    print(f'Going to {destination}!')
    destination = input()

    savings = 0
