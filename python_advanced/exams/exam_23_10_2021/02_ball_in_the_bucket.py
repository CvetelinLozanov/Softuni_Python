def is_index_valid(row, col, board):
    return 0 <= row < len(board) and 0 <= col < len(board)


def calculate_points(board, row, col, direction):
    points = 0
    for i in range(1, len(board)):
        current_row = row + direction[0] * i
        current_col = col + direction[1] * i

        if not is_index_valid(current_row, current_col, board):
            break

        points += int(board[current_row][current_col])

    return points


def calculate_opposite_points(board, row, col, direction):
    points = 0
    for i in range(1, len(board)):
        current_row = row - direction[0] * i
        current_col = col - direction[1] * i

        if not is_index_valid(current_row, current_col, board):
            break

        points += int(board[current_row][current_col])

    return points


board = [[line for line in input().split()] for _ in range(6)]
direction = (-1, 0)
total_sum = 0
award = ''

for _ in range(3):
    row, col = map(lambda x: int(x), input()[1:][:-1].split(', '))

    if not is_index_valid(row, col, board):
        continue

    if board[row][col] == 'B':
        total_sum += calculate_points(board, row, col, direction)
        total_sum += calculate_opposite_points(board, row, col, direction)
        board[row][col] = '-'

if 100 <= total_sum < 200:
    award = 'Football'
elif 200 <= total_sum < 300:
    award = 'Teddy Bear'
elif total_sum >= 300:
    award = 'Lego Construction Set'

if award != '':
    print(f"Good job! You scored {total_sum} points, and you've won {award}.")
else:
    print(f"Sorry! You need {100 - total_sum} points more to win a prize.")