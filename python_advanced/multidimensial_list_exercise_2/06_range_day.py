def is_valid_move(row, col, matrix):
    return 0 <= row < 5 and 0 <= col < 5 and matrix[row][col] == '.'


def is_valid_shot(row, col, matrix):
    return 0 <= row < 5 and 0 <= col < 5 and matrix[row][col] == 'x'


matrix = []
current_position = []
targets_count = 0
directions = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}
killed_targets = []

for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == 'A':
            current_position = [row, col]
        elif matrix[row][col] == 'x':
            targets_count += 1

initial_targets = targets_count
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()
    direction = command[1]

    if command[0] == 'shoot':
        row = current_position[0] + directions[direction][0]
        col = current_position[1] + directions[direction][1]
        while 0 <= row < 5 and 0 <= col < 5:
            if is_valid_shot(row, col, matrix):
                matrix[row][col] = '.'
                targets_count -= 1
                killed_targets.append([row, col])
                break
            row += directions[direction][0]
            col += directions[direction][1]

        if targets_count == 0:
            print(f'Training completed! All {len(killed_targets)} targets hit.')
            break

    elif command[0] == 'move':
        steps = int(command[2])
        row = current_position[0] + directions[direction][0] * steps
        col = current_position[1] + directions[direction][1] * steps

        if is_valid_move(row, col, matrix):
            matrix[current_position[0]][current_position[1]] = '.'
            matrix[row][col] = 'A'
            current_position[0] = row
            current_position[1] = col

if targets_count > 0:

    print(f'Training not completed! {targets_count} targets left.')

[print(x) for x in killed_targets]

