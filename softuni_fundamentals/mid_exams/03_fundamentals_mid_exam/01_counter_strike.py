def counter_strike():
    initial_energy = int(input())
    battles_won = 0
    while True:
        command = input()

        if command == 'End of battle':
            print(f'Won battles: {battles_won}. Energy left: {initial_energy}')
            break

        distance = int(command)

        if initial_energy >= distance:
            initial_energy -= distance
            battles_won += 1
            if battles_won % 3 == 0:
                initial_energy += battles_won
        else:
            print(f'Not enough energy! Game ends with {battles_won} won battles and {initial_energy} energy')
            break


counter_strike()