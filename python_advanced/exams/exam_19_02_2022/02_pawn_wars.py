def check_if_white_pawn_win(board, white_pawn_position_):
    next_white_pawn_row = white_pawn_position_[0] - 1
    current_white_pawn_col = white_pawn_position_[1]

    if next_white_pawn_row >= 0:
        if current_white_pawn_col - 1 >= 0:
            if board[next_white_pawn_row][current_white_pawn_col - 1] == 'b':
                return True
        if current_white_pawn_col + 1 <= 7:
            if board[next_white_pawn_row][current_white_pawn_col + 1] == 'b':
                return True

    return False


def check_if_black_pawn_win(board, black_pawn_position_):
    next_black_pawn_row = black_pawn_position_[0] + 1
    current_black_pawn_col = black_pawn_position_[1]

    if next_black_pawn_row <= 7:
        if current_black_pawn_col - 1 >= 0:
            if board[next_black_pawn_row][current_black_pawn_col - 1] == 'w':
                return True
        if current_black_pawn_col + 1 <= 7:
            if board[next_black_pawn_row][current_black_pawn_col + 1] == 'w':
                return True

    return False


sectors = [[f"{letter}{i}" for letter in 'abcdefgh'] for i in range(8, 0, -1)]
chess_board = []
white_pawn_position = []
black_pawn_position = []
turns = 0
is_white_pawn_winner = False
is_black_pawn_winner = False

for row in range(8):
    chess_board.append(input().split())
    for col in range(8):
        if chess_board[row][col] == 'w':
            white_pawn_position = [row, col]
        if chess_board[row][col] == 'b':
            black_pawn_position = [row, col]

while True:
    if turns % 2 == 0:
        is_white_pawn_winner = check_if_white_pawn_win(chess_board, white_pawn_position)
    else:
        is_black_pawn_winner = check_if_black_pawn_win(chess_board, black_pawn_position)

    if is_white_pawn_winner:
        print(f"Game over! White win, capture on {sectors[black_pawn_position[0]][black_pawn_position[1]]}.")
        break
    elif is_black_pawn_winner:
        print(f"Game over! Black win, capture on {sectors[white_pawn_position[0]][white_pawn_position[1]]}.")
        break

    if white_pawn_position[0] <= 0:
        print(f"Game over! White pawn is promoted to a queen at {sectors[white_pawn_position[0]][white_pawn_position[1]]}.")
        break
    elif black_pawn_position[0] >= 7:
        print(f"Game over! Black pawn is promoted to a queen at {sectors[black_pawn_position[0]][black_pawn_position[1]]}.")
        break

    if turns % 2 == 0:
        row, col = white_pawn_position
        next_row = row - 1
        chess_board[next_row][col] = 'w'
        chess_board[row][col] = '-'
        white_pawn_position = [next_row, col]

    else:
        row, col = black_pawn_position
        next_row = row + 1
        chess_board[next_row][col] = 'b'
        chess_board[row][col] = '-'
        black_pawn_position = [next_row, col]

    turns += 1