age_of_lily = int(input())
price_for_washing_machine = float(input())
price_for_toy = float(input())

toys = 0
cash = -10
lily_s_cash = 0
brother_money = -1

for age in range(age_of_lily + 1):
    if age % 2 == 0:
        cash += 10
        lily_s_cash += cash
        brother_money += 1
    else:
        toys += 1

total_cash = (lily_s_cash - brother_money) + toys * price_for_toy

if total_cash >= price_for_washing_machine:
    print(f'Yes! {total_cash - price_for_washing_machine:.2f}')
else:
    print(f'No! {abs(price_for_washing_machine - total_cash):.2f}')
