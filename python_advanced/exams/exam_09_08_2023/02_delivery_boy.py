def is_index_valid(row, col, row_len, col_len):
    return 0 <= row < row_len and 0 <= col < col_len


n, m = [int(num) for num in input().split(' ')]

field = []
current_position = []
initial_position = []
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
is_pizza_taken = False

for row in range(n):
    field.append(list(input()))
    for col in range(m):
        if field[row][col] == 'B':
            current_position = [row, col]
            initial_position = [row, col]

while True:
    direction = input()

    if direction in directions:
        row = current_position[0] + directions[direction][0]
        col = current_position[1] + directions[direction][1]

        if not is_index_valid(row, col, n, m):
            field[initial_position[0]][initial_position[1]] = ' '
            print(f"The delivery is late. Order is canceled.")
            break

        if field[row][col] == '*':
            continue

        if field[row][col] == 'P':
            print("Pizza is collected. 10 minutes for delivery.")
            field[row][col] = 'R'
            current_position = [row, col]
            is_pizza_taken = True
            continue

        if field[row][col] == 'A' and is_pizza_taken:
            field[row][col] = 'P'
            field[initial_position[0]][initial_position[1]] = 'B'
            print("Pizza is delivered on time! Next order...")
            break

        field[row][col] = '.'
        current_position = [row, col]


[print(''.join(line)) for line in field]