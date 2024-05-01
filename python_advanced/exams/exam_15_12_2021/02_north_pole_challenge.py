rows, cols = [int(num) for num in input().split(', ')]

field = []
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
current_position = []
decorations_count = 0
gifts_count = 0
cookies_count = 0

collected_decorations = 0
collected_gifts = 0
collected_cookies = 0
is_merry_christmas = False

for row in range(rows):
    field.append(input().split())
    for col in range(cols):
        if field[row][col] == 'Y':
            current_position = [row, col]
        elif field[row][col] == 'G':
            gifts_count += 1
        elif field[row][col] == 'D':
            decorations_count += 1
        elif field[row][col] == 'C':
            cookies_count += 1

while True:

    command = input()

    if command == 'End':
        break

    direction, steps = command.split('-')
    steps = int(steps)

    if direction in directions:
        for step in range(1, steps + 1):
            row = current_position[0] + directions[direction][0]
            col = current_position[1] + directions[direction][1]

            if row < 0:
                row = rows - 1

            elif row >= rows:
                row = 0

            if col < 0:
                col = cols - 1

            elif col >= cols:
                col = 0

            if field[row][col] == 'D':
                decorations_count -= 1
                collected_decorations +=1

            elif field[row][col] == 'G':
                gifts_count -= 1
                collected_gifts += 1

            elif field[row][col] == 'C':
                cookies_count -= 1
                collected_cookies += 1

            field[row][col] = 'Y'
            field[current_position[0]][current_position[1]] = 'x'
            current_position = [row, col]

            if cookies_count == 0 and decorations_count == 0 and gifts_count == 0:
                is_merry_christmas = True
                break

    if is_merry_christmas:
        print('Merry Christmas!')
        break

print("You've collected:")
print(f'- {collected_decorations} Christmas decorations')
print(f'- {collected_gifts} Gifts')
print(f'- {collected_cookies} Cookies')

[print(' '.join(line)) for line in field]