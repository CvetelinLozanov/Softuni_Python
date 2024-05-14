n = int(input())
car_number = input()
matrix = []
current_position = [0, 0]
tunnels_positions = []
kilometers_covered = 0
directions = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'T':
            tunnels_positions.append([row, col])

while True:
    direction = input()

    if direction == "End":
        matrix[current_position[0]][current_position[1]] = 'C'
        print(f"Racing car {car_number} DNF.")
        break

    if direction in directions:
        row, col = directions[direction][0] + current_position[0], directions[direction][1] + current_position[1]

        if matrix[row][col] == 'T':
            tunnels_positions.remove([row, col])
            matrix[row][col] = '.'
            row, col = tunnels_positions[0]
            matrix[row][col] = '.'
            current_position = [row, col]
            kilometers_covered += 30
            continue

        elif matrix[row][col] == 'F':
            kilometers_covered += 10
            matrix[row][col] = 'C'
            matrix[current_position[0]][current_position[1]] = '.'
            current_position = [row, col]
            print(f"Racing car {car_number} finished the stage!")
            break
        else:
            kilometers_covered += 10

        current_position = [row, col]


print(f"Distance covered {kilometers_covered} km.")
[print(''.join(line)) for line in matrix]