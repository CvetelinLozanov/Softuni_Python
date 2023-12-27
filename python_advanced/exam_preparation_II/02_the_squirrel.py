def is_valid_index(row, col, field):
    return 0 <= row < len(field) and 0 <= col < len(field)


n = int(input())
commands = [command for command in input().split(', ')]

field = []
squirrel_current_position = []
hazelnut_counter = 0
directions = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}
is_end = False

for row in range(n):
    field.append(list(input()))
    for col in range(n):
        if field[row][col] == 's':
            squirrel_current_position = [row, col]


for command in commands:
    if command in directions:
        row = squirrel_current_position[0] + directions[command][0]
        col = squirrel_current_position[1] + directions[command][1]

        if not is_valid_index(row, col, field):
            print('The squirrel is out of the field.')
            is_end = True
            break

        if field[row][col] == 't':
            print('Unfortunately, the squirrel stepped on a trap...')
            is_end = True
            break

        if field[row][col] == 'h':
            hazelnut_counter += 1
            field[squirrel_current_position[0]][squirrel_current_position[1]] = '*'
            field[row][col] = 's'

        squirrel_current_position[0], squirrel_current_position[1] = row, col

        if hazelnut_counter == 3:
            print('Good job! You have collected all hazelnuts!')
            break


if 0 <= hazelnut_counter < 3 and not is_end:
    print('There are more hazelnuts to collect.')

print(f'Hazelnuts collected: {hazelnut_counter}')