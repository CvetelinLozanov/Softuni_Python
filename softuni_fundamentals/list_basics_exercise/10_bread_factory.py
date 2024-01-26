energy = 100
coins = 100
events = input().split('|')
are_events_handled = True

for event in events:
    event_name, value = event.split('-')
    value = int(value)

    if event_name == 'rest':
        initial_energy = energy
        energy += value

        if energy > 100:
            energy = 100
        gained_energy = energy - initial_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')

    elif event_name == 'order':

        if energy >= 30:
            coins += value
            energy -= 30
            print(f'You earned {value} coins.')
            continue

        energy += 50
        print('You had to rest!')

    else:
        if coins >= value:
            coins -= value
            print(f'You bought {event_name}.')
        else:
            print(f'Closed! Cannot afford {event_name}.')
            are_events_handled = False
            break

if are_events_handled:
    print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')