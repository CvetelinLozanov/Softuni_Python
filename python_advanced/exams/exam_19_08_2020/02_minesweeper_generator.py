from typing import List


def is_index_valid(row, col, field_size):
    return 0 <= row < field_size and 0 <= col < field_size


def place_bombs(field_: List[List[int]], number_of_bombs_: int):
    for bomb_location in range(number_of_bombs_):
        [row, col] = map(lambda x: int(x), input()[1:][:-1].split(', '))
        if is_index_valid(row, col, len(field_)):
            field_[row][col] = '*'

    return field_


def fill_cells(row_, col_, field_):
    bomb_directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    for bomb_direction in bomb_directions:
        bomb_row = bomb_direction[0] + row_
        bomb_col = bomb_direction[1] + col_
        if is_index_valid(bomb_row, bomb_col, len(field_)) and field_[bomb_row][bomb_col] != '*':
            field_[bomb_row][bomb_col] += 1

    return field_


n = int(input())
number_of_bombs = int(input())
field = [[0 for _ in range(n)] for row in range(n)]

place_bombs(field, number_of_bombs)

for row in range(n):
    for col in range(n):
        if field[row][col] == '*':
            field = fill_cells(row, col, field)


[print(' '.join(map(str, row))) for row in field]
