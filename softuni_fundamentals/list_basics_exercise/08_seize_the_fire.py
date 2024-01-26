fire_level = input().split('#')

amount_of_water = int(input())
extinguished_fire = []
effort = 0

for fire in fire_level:
    fire_args = fire.split(' = ')
    type_of_fire = fire_args[0]
    fire_value = int(fire_args[1])

    if type_of_fire == 'Low':
        if 0 < fire_value <= 50:
            if amount_of_water >= fire_value:
                effort += fire_value * 0.25
                amount_of_water -= fire_value
                extinguished_fire.append(fire_value)

    elif type_of_fire == 'Medium':
        if 50 < fire_value <= 80:
            if amount_of_water >= fire_value:
                effort += fire_value * 0.25
                amount_of_water -= fire_value
                extinguished_fire.append(fire_value)

    elif type_of_fire == 'High':
        if 80 < fire_value <= 125:
            if amount_of_water >= fire_value:
                effort += fire_value * 0.25
                amount_of_water -= fire_value
                extinguished_fire.append(fire_value)

print('Cells:')
[print(f' - {ex_fire}') for ex_fire in extinguished_fire]
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(extinguished_fire)}')