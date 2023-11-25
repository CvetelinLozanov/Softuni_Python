money_for_vacation = float(input())
available_money = float(input())
number_of_spends = 0
number_of_days = 0

while available_money < money_for_vacation:
    command = input()
    current_money = float(input())
    number_of_days += 1

    if command == 'spend':
        if available_money < current_money:
            available_money = 0
        else:
            available_money -= current_money

        number_of_spends += 1
        if number_of_spends >= 5:
            print(f'You can\'t save the money.\n{number_of_days}')
            break

    if command == 'save':
        number_of_spends = 0
        available_money += current_money

else:
    print(f'You saved the money for {number_of_days} days.')