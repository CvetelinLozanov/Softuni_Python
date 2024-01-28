first_line = input().split()
second_line = input().split()
third_line = input().split()
board = first_line + second_line + third_line
is_first_player_won = False
is_second_player_won = False
start_index = 0
col_counter = 0
diagonal_counter = 0
columns = []
diagonal_1 = []
diagonal_2 = []
counter = 0

for index in range(len(board)):
    if index % 3 == 0:
        row = board[start_index:index]
        start_index = index
        if row.count('1') == 3:
            is_first_player_won = True
            break
        if row.count('2') == 3:
            is_second_player_won = True
            break
if not is_first_player_won and not is_second_player_won:
    for index in range(0, len(board) * 3, 3):
        col_counter += 1
        columns.append(board[index - counter])
        if col_counter % 3 == 0:
            if columns.count('1') == 3:
                is_first_player_won = True
                break
            if columns.count('2') == 3:
                is_second_player_won = True
                break
            columns.clear()
            counter += 8

if not is_first_player_won and not is_second_player_won:
    for index in range(0, len(board) // 2 + 1, 2):
        first_diagonal = board[index]
        diagonal_1.append(first_diagonal)
        second_diagonal = board[len(board) - 1 - index - 2]
        diagonal_2.append(second_diagonal)

    if diagonal_1.count('1') == 3:
        is_first_player_won = True
    if diagonal_1.count('2') == 3:
        is_second_player_won = True
    if diagonal_2.count('1') == 3:
        is_first_player_won = True
    if diagonal_2.count('2') == 3:
        is_second_player_won = True

if is_first_player_won:
    print('First player won')
elif is_second_player_won:
    print('Second player won')
else:
    print('Draw!')


# first_board_lines = input().split()
# second_board_lines = input().split()
# third_board_lines = input().split()
# have_winner = False
# whole_board = first_board_lines + second_board_lines + third_board_lines
# position_counter = 0
# step_index = 0
#
# while position_counter <= 2 and not have_winner:
#     winner_line = []
#     # first check consecutive positions 0,1,2 - 3,4,5 - 6,7,8
#     for h in range(position_counter * 3, (position_counter * 3) + 3):
#         winner_line.append(whole_board[h])
#
#     if winner_line.count("1") == 3:
#         have_winner = True
#         print("First player won")
#         break
#     elif winner_line.count("2") == 3:
#         have_winner = True
#         print("Second player won")
#         break
#
#     winner_line = []
#     # second, check consecutive positions 0,3,6 - 1,4,7 - 2,5,8
#     for v in range(position_counter, len(whole_board) + 1, 3):
#         if len(winner_line) < 3:
#             winner_line.append(whole_board[v])
#         else:
#             pass
#
#     if winner_line.count("1") == 3:
#         have_winner = True
#         print("First player won")
#         break
#     elif winner_line.count("2") == 3:
#         have_winner = True
#         print("Second player won")
#         break
#
#     winner_line = []
#     # second, check consecutive positions 0,4,8 - 2,4,6
#     if position_counter < 2:
#         for d in range(position_counter + position_counter, len(whole_board) + 1, 4 - (position_counter * 2)):
#             if len(winner_line) < 3:
#                 winner_line.append(whole_board[d])
#
#         if winner_line.count("1") == 3:
#             have_winner = True
#             print("First player won")
#             break
#         elif winner_line.count("2") == 3:
#             have_winner = True
#             print("Second player won")
#             break
#
#     position_counter += 1
#
# if not have_winner:
#     print("Draw!")

