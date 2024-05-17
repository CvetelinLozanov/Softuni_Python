def is_position_valid(row, row_len, col, col_len):
    return 0 <= row < row_len and 0 <= col < col_len


n, m = [int(num) for num in input().split()]
position = []
field = []
opponents_count = 0
moves_counter = 0
directions = {"down": (1, 0), "up": (-1, 0), "left": (0, -1), "right": (0, 1)}

for row in range(n):
    field.append(input().split())
    for col in range(m):
        if field[row][col] == 'B':
            position = [row, col]


while True:
    command = input()

    if command == 'Finish':
        break

    if command in directions:
        row = position[0] + directions[command][0]
        col = position[1] + directions[command][1]

        if not is_position_valid(row, n, col, m) or field[row][col] == 'O':
            continue

        if field[row][col] == 'P':
            opponents_count += 1

        moves_counter += 1
        field[row][col] = 'B'
        field[position[0]][position[1]] = '-'
        position = [row, col]

    if opponents_count == 3:
        break

print(f"Game over!")
print(f"Touched opponents: {opponents_count} Moves made: {moves_counter}")
