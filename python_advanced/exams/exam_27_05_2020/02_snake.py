def is_index_valid(row: int, col: int, field_length: int):
    return 0 <= row < field_length and 0 <= col < field_length


n = int(input())

field = []
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
burrows_positions = []
current_position = []
food_eaten = 0

for row in range(n):
    field.append(list(input()))
    for col in range(n):
        if field[row][col] == 'S':
            current_position = [row,col]
        elif field[row][col] == 'B':
            burrows_positions.append((row, col))


while True:
    command = input()

    if command in directions:
        row, col = directions[command][0] + current_position[0], directions[command][1] + current_position[1]

        if not is_index_valid(row, col, n):
            field[current_position[0]][current_position[1]] = '.'
            print("Game over!")
            break

        if field[row][col] == '*':
            food_eaten += 1

        elif field[row][col] == 'B':
            current_burrow_position = (row, col)
            if current_burrow_position in burrows_positions:
                burrows_positions.remove(current_burrow_position)
                field[current_burrow_position[0]][current_burrow_position[1]] = '.'
                current_burrow_position = burrows_positions[0]
                row, col = current_burrow_position

        field[current_position[0]][current_position[1]] = '.'
        field[row][col] = 'S'
        current_position = [row, col]

        if food_eaten == 10:
            print("You won! You fed the snake.")
            break

print(f"Food eaten: {food_eaten}")
[print(''.join(row)) for row in field]