n = int(input())
matrix = []
current_position = []
hive_position = []
initial_energy = 15
directions = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}
nectar_collected = 0
revive_count = 0
is_on_hive = False

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 'B':
            current_position = [row, col]
        if matrix[row][col] == 'H':
            hive_position = [row, col]


row, col = current_position
while True:

    direction = input()

    if direction in directions:
        row += directions[direction][0]
        col += directions[direction][1]
        initial_energy -= 1

        if row >= n:
            row = 0
        elif row < 0:
            row = n - 1

        if col >= n:
            col = 0
        elif col < 0:
            col = n - 1

        if initial_energy <= 0 and nectar_collected < 30:
            break

        if initial_energy <= 0 and nectar_collected >= 30 and revive_count < 1:
            initial_energy += nectar_collected - 30
            nectar_collected = 30
            revive_count += 1

        if matrix[row][col].isdigit():
            nectar_collected += int(matrix[row][col])
            matrix[row][col] = '-'

        if matrix[row][col] == 'H':
            is_on_hive = True
            break

        if initial_energy <= 0:
            break

matrix[current_position[0]][current_position[1]] = '-'
matrix[row][col] = 'B'

if is_on_hive and nectar_collected >= 30:
    print(f"Great job, Beesy! The hive is full. Energy left: {initial_energy}")
elif is_on_hive and nectar_collected < 30:
    print("Beesy did not manage to collect enough nectar.")
elif not is_on_hive:
    print("This is the end! Beesy ran out of energy.")

[print(''.join(line)) for line in matrix]



