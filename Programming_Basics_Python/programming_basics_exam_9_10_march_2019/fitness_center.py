number_of_clients = int(input())

back_trainings = 0
chest_trainings = 0
legs_trainings = 0
abs_trainings = 0
total_clients = 0
protein_shake_buys = 0
protein_bars_buys = 0

for client in range(number_of_clients):
    type_of_training = input()

    if type_of_training == 'Back':
        back_trainings += 1
        total_clients += 1

    elif type_of_training == 'Chest':
        chest_trainings += 1
        total_clients += 1

    elif type_of_training == 'Legs':
        legs_trainings += 1
        total_clients += 1

    elif type_of_training == 'Abs':
        abs_trainings += 1
        total_clients += 1

    elif type_of_training == 'Protein shake':
        protein_shake_buys += 1

    elif type_of_training == 'Protein bar':
        protein_bars_buys += 1

buyers = number_of_clients - total_clients

print(f'{back_trainings} - back')
print(f'{chest_trainings} - chest')
print(f'{legs_trainings} - legs')
print(f'{abs_trainings} - abs')
print(f'{protein_shake_buys} - protein shake')
print(f'{protein_bars_buys} - protein bar')
print(f'{total_clients / number_of_clients * 100:.2f}% - work out')
print(f'{buyers / number_of_clients * 100:.2f}% - protein')
