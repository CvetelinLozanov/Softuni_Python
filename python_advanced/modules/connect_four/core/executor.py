from modules.connect_four.core.board_initializer import initialize_game_board, print_matrix, COLS
from modules.connect_four.core.winner_checks import is_winner
from modules.connect_four.core.player_choice_validations import is_valid_column_choice, place_player_number, FullColumnError

def play_connect_four_game():
    matrix = initialize_game_board()

    player = 1
    while True:
        try:
            selected_column_number = int(input(f"Player {player}, please choose a column: "))
            selected_column_index = selected_column_number - 1
            if not is_valid_column_choice(selected_column_index):
                raise ValueError
            current_row, current_col = place_player_number(selected_column_index, matrix, player)
            if is_winner(current_row, current_col, matrix, player):
                print(f"Player {player} wins!")
                print_matrix(matrix)
                break
            print_matrix(matrix)
        except ValueError:
            print(f"Player {player}, please select number between 1 and {COLS}")
            continue
        except FullColumnError:
            print(f"Player {player}, this column is full, please select another one")
            continue

        player += 1
        player = 2 if player % 2 == 0 else 1