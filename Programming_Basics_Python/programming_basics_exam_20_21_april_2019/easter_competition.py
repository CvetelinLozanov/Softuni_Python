number_of_easter_breads = int(input())

best_baker = ''
highest_result = 0
baker_points = 0

for _ in range(number_of_easter_breads):
    baker_name = input()

    while True:
        text = input()

        if text == 'Stop':
            break

        points = int(text)

        baker_points += points

    print(f'{baker_name} has {baker_points} points.')

    if baker_points > highest_result:
        highest_result = baker_points
        best_baker = baker_name
        print(f'{baker_name} is the new number 1!')

    baker_points = 0

print(f'{best_baker} won competition with {highest_result} points!')