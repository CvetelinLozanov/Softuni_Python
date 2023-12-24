ROWS = 6
COLS = 7


def print_matrix(matrix):
    for row in matrix:
        print(row)


def initialize_game_board():
    matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    print_matrix(matrix)
    return matrix