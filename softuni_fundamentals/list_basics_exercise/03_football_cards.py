team_a = [str(el) for el in range(1, 12)]
team_b = [str(el) for el in range(1, 12)]

cards = input().split()
is_game_terminated = False

for card in cards:
    team, player = card.split('-')

    if team == 'A':
        if player in team_a:
            team_a.remove(player)

    elif team == 'B':
        if player in team_b:
            team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:
        is_game_terminated = True
        break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')

if is_game_terminated:
    print('Game was terminated')