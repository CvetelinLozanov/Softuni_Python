from modules.connect_four.core.player_choice_validations import is_valid_column_choice, is_valid_place, place_player_number


direction_mapper = [
    (-1, 0),  # Up
    (0, 1),  # Right
    (-1, 1),  # Up right
    (-1, -1),  # Up left
]


def requested_direction_count(current_row, current_col, row_movement, col_movement, matrix, player):
    count = 0
    for i in range(1, 4):
        row_index_to_check = current_row + row_movement * i
        col_index_to_check = current_col + col_movement * i
        if not is_valid_place(row_index_to_check, col_index_to_check):
            break
        if matrix[row_index_to_check][col_index_to_check] != player:
            break
        count += 1
    return count


def opposite_direction_count(current_row, current_col, row_movement, col_movement, matrix, player):
    count = 0
    for i in range(1, 4):
        row_index_to_check = current_row - row_movement * i
        col_index_to_check = current_col - col_movement * i
        if not is_valid_place(row_index_to_check, col_index_to_check):
            break
        if matrix[row_index_to_check][col_index_to_check] != player:
            break
        count += 1
    return count


def is_winner(current_row, current_col, matrix, player):
    for row_movement, col_movement in direction_mapper:
        count_direction = requested_direction_count(current_row, current_col, row_movement, col_movement, matrix,
                                                    player)
        count_opposite_direction = opposite_direction_count(current_row, current_col, row_movement, col_movement,
                                                            matrix, player)
        if (count_direction + count_opposite_direction) >= 3:
            return True
    return False
