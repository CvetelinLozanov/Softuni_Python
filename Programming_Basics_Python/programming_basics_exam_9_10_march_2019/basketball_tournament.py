name_of_tournament = input()
played_matches = 0
won_matches = 0
lose_matches = 0
total_matches = 0

while name_of_tournament != 'End of tournaments':
    number_of_matches = int(input())
    total_matches += number_of_matches

    for match in range(number_of_matches):
        played_matches += 1
        desi_s_team_points = int(input())
        opponent_team_points = int(input())

        if desi_s_team_points > opponent_team_points:
            won_matches += 1
            print(f'Game {played_matches} of tournament {name_of_tournament}: win with {desi_s_team_points - opponent_team_points} points.')

        else:
            lose_matches += 1
            print(f'Game {played_matches} of tournament {name_of_tournament}: lost with {opponent_team_points - desi_s_team_points} points.')

    name_of_tournament = input()
    played_matches = 0

print(f'{won_matches / total_matches * 100:.2f}% matches win')
print(f'{lose_matches / total_matches * 100:.2f}% matches lost')
