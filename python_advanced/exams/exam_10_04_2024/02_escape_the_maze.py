def is_index_valid(row, col, field_size):
    return 0 <= row < field_size and 0 <= col < field_size


n = int(input())

field = []
current_position = []
health = 100
is_escaped = False
directions = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}

for row in range(n):
    field.append(list(input()))
    for col in range(n):
        if field[row][col] == 'P':
            current_position = [row, col]


while True:
    command = input()

    if command in directions:
        row = directions[command][0] + current_position[0]
        col = directions[command][1] + current_position[1]

        if not is_index_valid(row, col, n):
            continue

        if field[row][col] == 'M':
            health -= 40

        elif field[row][col] == 'H':
            health += 15
            if health > 100:
                health = 100

        elif field[row][col] == 'X':
            print('Player escaped the maze. Danger passed!')
            is_escaped = True

        field[current_position[0]][current_position[1]] = '-'
        field[row][col] = 'P'
        current_position = [row, col]

        if is_escaped:
            break

        if health <= 0:
            health = 0
            print('Player is dead. Maze over!')
            break

print(f"Player's health: {health} units")
[print(''.join(line)) for line in field]
