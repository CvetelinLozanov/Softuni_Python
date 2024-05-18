n = int(input())

current_position = []
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
total_fish_caught = 0
field = []
is_in_whirlpool = False


for row in range(n):
    field.append(list(input()))
    for col in range(n):
        if field[row][col] == 'S':
            current_position = [row, col]


while True:
    command = input()

    if command == 'collect the nets':
        break

    if command in directions:
        row = current_position[0] + directions[command][0]
        col = current_position[1] + directions[command][1]
        if row < 0:
            row = n - 1

        elif row == n:
            row = 0

        if col < 0:
            col = n - 1

        elif col == n:
            col = 0

        if field[row][col] == 'W':
            print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught."
                  f" Last coordinates of the ship: [{row},{col}]")
            is_in_whirlpool = True
            break

        if field[row][col].isdigit():
            total_fish_caught += int(field[row][col])

        field[current_position[0]][current_position[1]] = '-'
        field[row][col] = 'S'
        current_position = [row, col]

if total_fish_caught >= 20 and not is_in_whirlpool:
    print("Success! You managed to reach the quota!")

elif total_fish_caught < 20 and not is_in_whirlpool:
    print(f"You didn't catch enough fish and didn't reach the quota!"
          f" You need {20 - total_fish_caught} tons of fish more.")

if total_fish_caught > 0 and not is_in_whirlpool:
    print(f"Amount of fish caught: {total_fish_caught} tons.")

if not is_in_whirlpool:
    [print(''.join(line)) for line in field]