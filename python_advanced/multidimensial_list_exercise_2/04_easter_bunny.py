def is_valid(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix) and matrix[row][col] != 'X'


def eggs_collected_per_direction(direction_sum, direction, matrix, row, col):
    if direction not in direction_sum:
        direction_sum[direction] = 0
    direction_sum[direction] += int(matrix[row][col])
    return direction_sum


def eggs_indexes(direction_indexes, direction, row, col):
    if direction not in direction_indexes:
        direction_indexes[direction] = []
    direction_indexes[direction].append([row, col])
    return direction_indexes


n = int(input())

start_row = None
start_col = None
matrix = []
direction = None
direction_sum = {}
direction_indexes = {}

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'B':
            start_row = row
            start_col = col

for row in range(start_row - 1, -1, -1):
    if is_valid(row, start_col, matrix):
        direction = 'up'
        direction_sum = eggs_collected_per_direction(direction_sum, direction, matrix, row, start_col)
        direction_indexes = eggs_indexes(direction_indexes, direction, row, start_col)
    else:
        break

for row in range((start_row + 1), n):
    if is_valid(row, start_col, matrix):
        direction = 'down'
        direction_sum = eggs_collected_per_direction(direction_sum, direction, matrix, row, start_col)
        direction_indexes = eggs_indexes(direction_indexes, direction, row, start_col)
    else:
        break

for col in range(start_col + 1, n):
    if is_valid(start_row, col, matrix):
        direction = 'right'
        direction_sum = eggs_collected_per_direction(direction_sum, direction, matrix, start_row, col)
        direction_indexes = eggs_indexes(direction_indexes, direction, start_row, col)
    else:
        break

for col in range(start_col - 1, -1, -1):
    if is_valid(start_row, col, matrix):
        direction = 'left'
        direction_sum = eggs_collected_per_direction(direction_sum, direction, matrix, start_row, col)
        direction_indexes = eggs_indexes(direction_indexes, direction, start_row, col)
    else:
        break

max_value = max(direction_sum.values())
direction_with_max_sum = list(direction_sum.keys())[list(direction_sum.values()).index(max_value)]
print(direction_with_max_sum)
[print(x) for x in direction_indexes[direction_with_max_sum]]
print(max_value)