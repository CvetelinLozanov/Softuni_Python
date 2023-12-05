from collections import deque

water_quantity = int(input())
person_name = input()
people_for_water = deque()

while person_name != 'Start':
    people_for_water.append(person_name)
    person_name = input()

command = input()

while command != 'End':
    command_args = command.split()
    command_length = len(command_args)

    if command_length == 1:
        name = people_for_water.popleft()
        liters_to_drink = int(command_args[0])
        if liters_to_drink <= water_quantity:

            print(f'{name} got water')
            water_quantity -= liters_to_drink
        else:
            print(f'{name} must wait')

    else:
        water_quantity += int(command_args[1])

    command = input()

print(f'{water_quantity} liters left')