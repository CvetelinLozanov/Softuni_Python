from math import floor


matrix = []

n = int(input())
current_position = []
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
coins = 0


for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'P':
            current_position = [row, col]

        elif matrix[row][col] != 'P' and matrix[row][col] != 'X':
            matrix[row][col] = int(matrix[row][col])

path = [[current_position[0], current_position[1]]]

while coins < 100:

    command = input()

    if command in directions:
        row = current_position[0] + directions[command][0]
        col = current_position[1] + directions[command][1]

        if row < 0:
            row = len(matrix) - 1

        elif row >= len(matrix):
            row = 0

        if col < 0:
            col = len(matrix) - 1

        elif col >= len(matrix):
            col = 0

        path.append([row, col])

        if matrix[row][col] == 'X':
            coins = floor(coins / 2)
            print(f"Game over! You've collected {coins} coins.")
            break

        coins += matrix[row][col]

        matrix[current_position[0]][current_position[1]] = 0
        matrix[row][col] = 'P'
        current_position = [row, col]

else:
    print(f"You won! You've collected {coins} coins.")

print("Your path:")
[print(p) for p in path]