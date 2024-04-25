def is_index_valid(row, col, field_size):
    return 0 <= row < field_size and 0 <= col < field_size

word = input()

directions = { "up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1) }
n = int(input())
field = []
current_position = []
for row in range(n):
    field.append(list(input()))
    for col in range(n):
        if field[row][col] == 'P':
            current_position = [row, col]

m = int(input())

for _ in range(m):
    command = input()

    if command in directions:
        row = directions[command][0] + current_position[0]
        col = directions[command][1] + current_position[1]

        if not is_index_valid(row, col, n):
            if word:
                word = word[:-1]
            continue

        if field[row][col].isalpha():
            word += field[row][col]

        field[current_position[0]][current_position[1]] = '-'
        field[row][col] = 'P'
        current_position = [row, col]

print(word)
[print(''.join(line)) for line in field]