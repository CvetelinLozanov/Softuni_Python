def is_valid(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col


rows, cols = [int(x) for x in input().split(',')]

cupboard = []
current_mouse_position = []
cheese_counter = 0
directions = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}


for row in range(rows):
    cupboard.append(list(input()))
    for col in range(cols):
        if cupboard[row][col] == 'M':
            current_mouse_position = [row, col]
        elif cupboard[row][col] == 'C':
            cheese_counter += 1

while True:
    command = input()
    if command == 'danger':
        print('Mouse will come back later!')
        break

    if command in directions:
        row = current_mouse_position[0] + directions[command][0]
        col = current_mouse_position[1] + directions[command][1]

        if not is_valid(row, col, rows, cols):
            print('No more cheese for tonight!')
            break

        if cupboard[row][col] == 'C':
            cheese_counter -= 1
            cupboard[current_mouse_position[0]][current_mouse_position[1]] = '*'
            cupboard[row][col] = 'M'
            current_mouse_position[0], current_mouse_position[1] = row, col

        elif cupboard[row][col] == 'T':
            cupboard[current_mouse_position[0]][current_mouse_position[1]] = '*'
            cupboard[row][col] = 'M'
            current_mouse_position[0], current_mouse_position[1] = row, col
            print('Mouse is trapped!')
            break

        elif cupboard[row][col] == '@':
            continue

        cupboard[current_mouse_position[0]][current_mouse_position[1]] = '*'
        cupboard[row][col] = 'M'
        current_mouse_position[0], current_mouse_position[1] = row, col

    if cheese_counter == 0:
        print('Happy mouse! All the cheese is eaten, good night!')
        break


[print(''.join(el)) for el in cupboard]
