players = input().split(', ')
players_dict = {player: {"is_resting": False} for player in players}

turn = 1

matrix = [[line for line in input().split()] for _ in range(6)]

while True:
    current_player = players[0] if turn % 2 != 0 else players[1]
    [row, col] = map(lambda x: int(x), input()[1:-1].split(', '))

    if players_dict[current_player]['is_resting']:
        players_dict[current_player]['is_resting'] = False
        turn += 1
        continue

    next_player = players[0] if turn % 2 == 0 else players[1]

    if matrix[row][col] == 'E':
        print(f"{current_player} found the Exit and wins the game!")
        break

    elif matrix[row][col] == 'T':
        print(f"{current_player} is out of the game! The winner is {next_player}.")
        break

    elif matrix[row][col] == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        players_dict[current_player]['is_resting'] = True

    turn += 1