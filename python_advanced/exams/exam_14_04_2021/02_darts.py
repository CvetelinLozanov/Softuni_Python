def is_index_valid(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def calculate_hit(row, col, direction_mapper, multiplier, matrix):
    total_sum = 0
    for mapper_row, mapper_col in direction_mapper:
        for i in range(1, len(matrix)):
            current_row = row + mapper_row * i
            current_col = col + mapper_col * i

            if not is_index_valid(current_row, current_col, matrix):
                break

            if matrix[current_row][current_col].isdigit():
                total_sum += int(matrix[current_row][current_col])
                break

    return total_sum * multiplier


def calculate_opposite_hit(row, col, direction_mapper, multiplier, matrix):
    total_sum = 0
    for mapper_row, mapper_col in direction_mapper:
        for i in range(1, len(matrix)):
            current_row = row - mapper_row * i
            current_col = col - mapper_col * i

            if not is_index_valid(current_row, current_col, matrix):
                break

            if matrix[current_row][current_col].isdigit():
                total_sum += int(matrix[current_row][current_col])
                break

    return total_sum * multiplier


player_one, player_two = input().split(', ')
player_one_points = 501
player_two_points = 501
player_one_throws = 0
player_two_throws = 0
matrix = [[line for line in input().split()] for _ in range(7)]
direction_mapper = [(-1, 0), (0, 1)]
turn = 0

while player_one_points > 0 and player_two_points > 0:
    row, col = [int(el) for el in input()[1:][:-1].split(', ')]
    turn += 1

    if turn % 2 != 0:
        player_one_throws += 1
    else:
        player_two_throws += 1

    if not is_index_valid(row, col, matrix):
        continue

    if matrix[row][col] == 'B':
        if turn % 2 != 0:
            player_one_points = 0
        else:
            player_two_points = 0
        break

    if matrix[row][col].isdigit():
        if turn % 2 != 0:
            player_one_points -= int(matrix[row][col])
        else:
            player_two_points -= int(matrix[row][col])

    elif matrix[row][col] == 'D':
        if turn % 2 != 0:
            player_one_points -= calculate_hit(row, col, direction_mapper, 2, matrix)
            player_one_points -= calculate_opposite_hit(row, col, direction_mapper, 2, matrix)
        else:
            player_two_points -= calculate_hit(row, col, direction_mapper, 2, matrix)
            player_two_points -= calculate_opposite_hit(row, col, direction_mapper, 2, matrix)

    elif matrix[row][col] == 'T':
        if turn % 2 != 0:
            player_one_points -= calculate_hit(row, col, direction_mapper, 3, matrix)
            player_one_points -= calculate_opposite_hit(row, col, direction_mapper, 3, matrix)
        else:
            player_two_points -= calculate_hit(row, col, direction_mapper, 3, matrix)
            player_two_points -= calculate_opposite_hit(row, col, direction_mapper, 3, matrix)

if player_one_points <= 0:
    print(f"{player_one} won the game with {player_one_throws} throws!")
else:
    print(f"{player_two} won the game with {player_two_throws} throws!")