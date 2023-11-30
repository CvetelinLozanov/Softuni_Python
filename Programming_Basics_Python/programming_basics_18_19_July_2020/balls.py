from math import floor

number_of_balls = int(input())
total_points = 0
red_counter = 0
orange_counter = 0
yellow_counter = 0
white_counter = 0
divided_counter = 0
other_colors_counter = 0

for ball in range(number_of_balls):

    ball_color = input()

    if ball_color == 'red':
        red_counter += 1
        total_points += 5

    elif ball_color == 'orange':
        orange_counter += 1
        total_points += 10

    elif ball_color == 'yellow':
        yellow_counter += 1
        total_points += 15

    elif ball_color == 'white':
        white_counter += 1
        total_points += 20

    elif ball_color == 'black':
        divided_counter += 1
        total_points = floor(total_points / 2)

    else:
        other_colors_counter += 1
        continue

print(f'Total points: {total_points}')
print(f'Red balls: {red_counter}')
print(f'Orange balls: {orange_counter}')
print(f'Yellow balls: {yellow_counter}')
print(f'White balls: {white_counter}')
print(f'Other colors picked: {other_colors_counter}')
print(f'Divides from black balls: {divided_counter}')