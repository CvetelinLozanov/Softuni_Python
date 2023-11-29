hall_capacity = int(input())
tickets_profit = 0
command = input()

while command != 'Movie time!':

    people = int(command)
    if people > hall_capacity:
        print('The cinema is full.')
        break

    tickets_profit += people * 5

    if people % 3 == 0:
        tickets_profit -= 5

    hall_capacity -= people

    command = input()

else:
    print(f'There are {hall_capacity} seats left in the cinema.')

print(f'Cinema income - {tickets_profit} lv.')
