from math import floor

number_of_tournaments = int(input())
starting_points = int(input())
points_for_tournament = 0
victories = 0

for _ in range(number_of_tournaments):

    tournament_result = input()

    if tournament_result == 'W':
        points_for_tournament += 2000
        victories += 1

    elif tournament_result == 'F':
        points_for_tournament += 1200

    elif tournament_result == 'SF':
        points_for_tournament += 720

final_points = starting_points + points_for_tournament

print(f'Final points: {final_points}')
print(f'Average points: {floor(points_for_tournament / number_of_tournaments)}')
print(f'{victories / number_of_tournaments * 100:.2f}%')