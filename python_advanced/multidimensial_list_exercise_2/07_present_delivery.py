def is_valid(row, col, matrix):
    return 0 <= row < len(matrix) or 0 <= col < len(matrix)


number_of_presents = int(input())
n = int(input())
matrix = []
current_position = []
nice_kids_counter = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'S':
            current_position = [row, col]
        elif matrix[row][col] == 'V':
            nice_kids_counter += 1
initial_nice_kids = nice_kids_counter
directions = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}


while number_of_presents > 0:

    command = input()

    if command == 'Christmas morning':
        break

    if command in directions:
        row = current_position[0] + directions[command][0]
        col = current_position[1] + directions[command][1]

        if is_valid(row, col, matrix) and matrix[row][col] == 'X':
            matrix[current_position[0]][current_position[1]] = '-'
            matrix[row][col] = 'S'
            current_position[0], current_position[1] = row, col

        elif is_valid(row, col, matrix) and matrix[row][col] == 'V':
            matrix[current_position[0]][current_position[1]] = '-'
            matrix[row][col] = 'S'
            number_of_presents -= 1
            nice_kids_counter -= 1
            current_position[0], current_position[1] = row, col

        elif is_valid(row, col, matrix) and matrix[row][col] == 'C':
            matrix[current_position[0]][current_position[1]] = '-'
            matrix[row][col] = 'S'
            if is_valid(row + 1, col, matrix) and (matrix[row + 1][col] == 'V' or matrix[row + 1][col] == 'X') and number_of_presents > 0:
                if matrix[row + 1][col] == 'V':
                    nice_kids_counter -= 1
                number_of_presents -= 1
                matrix[row + 1][col] = '-'
            if is_valid(row - 1, col, matrix) and (matrix[row - 1][col] == 'V' or matrix[row - 1][col] == 'X') and number_of_presents > 0:
                if matrix[row - 1][col] == 'V':
                    nice_kids_counter -= 1
                number_of_presents -= 1
                matrix[row - 1][col] = '-'
            if is_valid(row, col + 1, matrix) and (matrix[row][col + 1] == 'V' or matrix[row][col + 1] == 'X') and number_of_presents > 0:
                if matrix[row][col + 1] == 'V':
                    nice_kids_counter -= 1
                number_of_presents -= 1
                matrix[row][col + 1] = '-'
            if is_valid(row, col - 1, matrix) and (matrix[row][col - 1] == 'V' or matrix[row][col - 1] == 'X') and number_of_presents > 0:
                if matrix[row][col - 1] == 'V':
                    nice_kids_counter -= 1
                number_of_presents -= 1
                matrix[row][col - 1] = '-'
            current_position[0], current_position[1] = row, col

        else:
            matrix[current_position[0]][current_position[1]] = '-'
            matrix[row][col] = 'S'
            current_position[0], current_position[1] = row, col

if number_of_presents == 0 and nice_kids_counter > 0:
    print('Santa ran out of presents!')

[print(*line) for line in matrix]

if nice_kids_counter == 0:
    print(f'Good job, Santa! {initial_nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids_counter} nice kid/s.')
