clients = int(input())

total_costs = 0
items_counter = 0
client_costs = 0

for _ in range(clients):

    command = input()
    while command != 'Finish':
        if command == 'basket':
            items_counter += 1
            client_costs += 1.50

        elif command == 'wreath':
            items_counter += 1
            client_costs += 3.80

        elif command == 'chocolate bunny':
            items_counter += 1
            client_costs += 7

        command = input()

    else:

        if items_counter % 2 == 0:
            client_costs *= 0.80

        total_costs += client_costs
        print(f'You purchased {items_counter} items for {client_costs:.2f} leva.')

    client_costs = 0
    items_counter = 0

print(f'Average bill per client is: {total_costs / clients:.2f} leva.')

