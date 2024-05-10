def process_commands(matrix_, text_, prompt_row, prompt_col, directions_):

    command, direction = text_.split(', ')[0:2]

    current_row = prompt_row + directions_[direction][0]
    current_col = prompt_col + directions_[direction][1]

    if command == "Create":
        value = text_.split(', ')[2]
        if matrix_[current_row][current_col] == '.':
            matrix_[current_row][current_col] = value

    elif command == "Update":
        value = text_.split(', ')[2]
        if matrix_[current_row][current_col] != '.':
            matrix_[current_row][current_col] = value

    elif command == 'Delete':
        if matrix_[current_row][current_col] != '.':
            matrix_[current_row][current_col] = '.'

    elif command == 'Read':
        if matrix_[current_row][current_col] != '.':
            print(matrix_[current_row][current_col])

    return matrix_, current_row, current_col


matrix = [[line for line in input().split()] for _ in range(6)]

[current_row, current_col] = [int(num) for num in input()[1:-1].split(', ')]
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    text = input()

    if text == 'Stop':
         break

    matrix, current_row, current_col = process_commands(matrix, text, current_row, current_col, directions)


[print(*line) for line in matrix]