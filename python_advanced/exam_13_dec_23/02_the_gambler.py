def is_in_board(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


n = int(input())

initial_cash = 100
board = []
current_position = []
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
is_jackpot_won = False

for row in range(n):
    row_data = list(input())
    if 'G' in row_data:
        col = row_data.index('G')
        current_position = [row, col]
    board.append(row_data)

direction = input()

while direction != 'end':
    if direction in directions:
        row, col = current_position[0] + directions[direction][0], current_position[1] + directions[direction][1]
        if not is_in_board(row, col, board):
            print('Game over! You lost everything!')
            break

        desired_field = board[row][col]
        board[current_position[0]][current_position[1]] = '-'
        board[row][col] = 'G'
        current_position[0],current_position[1] = row, col

        if desired_field == 'W':
            initial_cash += 100

        elif desired_field == 'P':
            initial_cash -= 200

        elif desired_field == 'J':
            initial_cash += 100000
            print(f'You win the Jackpot!\nEnd of the game. Total amount: {initial_cash}$')
            break

        if initial_cash <= 0:
            print('Game over! You lost everything!')
            break

    direction = input()
else:
    print(f'End of the game. Total amount: {initial_cash}$')

if initial_cash > 0:
   [print(''.join(el)) for el in board]
