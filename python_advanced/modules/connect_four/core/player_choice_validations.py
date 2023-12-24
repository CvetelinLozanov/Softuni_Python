from modules.connect_four.core.board_initializer import ROWS, COLS


class FullColumnError(Exception):
    pass


def is_valid_column_choice(selected_column_index):
    return 0 <= selected_column_index < COLS


def place_player_number(column_index, matrix, player_number):
    for row_index in range(ROWS - 1, -1, -1):
        if matrix[row_index][column_index] == 0:
            matrix[row_index][column_index] = player_number
            return row_index, column_index
    else:
        raise FullColumnError


def is_valid_place(row, col):
    return 0 <= row < ROWS and 0 <= col < COLS