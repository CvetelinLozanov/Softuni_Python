def is_index_valid(row, col, board_size):
    return 0 <= row < len(board_size) and 0 <= col < len(board_size)


def get_king_position(king_position_):
    for row in range(8):
        for col in range(8):
            if board[row][col] == 'K':
                king_position_ = [row, col]

    return king_position_


def check_positions(king_position_, board_, queens_positions_, row_direction_, col_direction_):
    for i in range(1, len(board_)):
        row_index_to_check = king_position[0] + row_direction_ * i
        col_index_to_check = king_position_[1] + col_direction_ * i

        if not is_index_valid(row_index_to_check, col_index_to_check, board_):
            break

        if board_[row_index_to_check][col_index_to_check] == 'Q':
            queens_positions_.append([row_index_to_check, col_index_to_check])
            break

    return queens_positions_


def check_opposite_positions(king_position_, board_, queens_positions_, row_direction_, col_direction_):
    for i in range(1, len(board_)):
        row_index_to_check = king_position[0] - row_direction_ * i
        col_index_to_check = king_position_[1] - col_direction_ * i

        if not is_index_valid(row_index_to_check, col_index_to_check, board_):
            break

        if board_[row_index_to_check][col_index_to_check] == 'Q':
            queens_positions_.append([row_index_to_check, col_index_to_check])
            break

    return queens_positions_


board = [[item for item in input().split()] for line in range(8)]

king_position = []
queens_positions = []
direction_mapper = [
    (0, 1),  # Right
    (-1, 0),  # Up
    (-1, -1),  # Up left
    (-1, 1),  # Up right
]
king_position = get_king_position(king_position)

for row_direction, col_direction in direction_mapper:
    queens_positions = check_positions(king_position, board, queens_positions, row_direction, col_direction)
    queens_positions = check_opposite_positions(king_position, board, queens_positions, row_direction, col_direction)

if queens_positions:
    [print(position) for position in queens_positions]
else:
    print("The king is safe!")

