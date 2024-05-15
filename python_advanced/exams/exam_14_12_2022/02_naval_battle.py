n = int(input())

current_position = []
field = []
submarine_life = 2
battle_cruisers = 3
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for row in range(n):
    field.append(list(input()))
    for col in range(n):
        if field[row][col] == 'S':
            current_position = [row, col]

while True:
    direction = input()

    if direction in directions:
        row = directions[direction][0] + current_position[0]
        col = directions[direction][1] + current_position[1]

        if field[row][col] == '*':
            submarine_life -= 1

        elif field[row][col] == 'C':
            battle_cruisers -= 1

        field[current_position[0]][current_position[1]] = '-'
        field[row][col] = 'S'
        current_position = [row, col]

        if submarine_life < 0:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
            break

        if battle_cruisers == 0:
            print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

[print(''.join(line)) for line in field]


