field = []
current_position = []
water_deposits_count = 0
metal_deposits_count = 0
concrete_deposits_count = 0
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for row in range(6):
    field.append(input().split())
    for col in range(6):
        if field[row][col] == 'E':
            current_position = [row, col]

commands = input().split(', ')

for command in commands:
    if command in directions:
        row = current_position[0] + directions[command][0]
        col = current_position[1] + directions[command][1]

        if row < 0:
            row = 5
        elif row > 5:
            row = 0

        if col < 0:
            col = 5
        elif col > 5:
            col = 0

        material = ''

        if field[row][col] == 'R':
            print(f"Rover got broken at ({row}, {col})")
            break

        elif field[row][col] == 'W':
            water_deposits_count += 1
            material = "Water"

        elif field[row][col] == 'M':
            metal_deposits_count += 1
            material = "Metal"

        elif field[row][col] == 'C':
            concrete_deposits_count += 1
            material = "Concrete"

        if material != '':
            print(f"{material} deposit found at ({row}, {col})")

        field[row][col] = 'E'
        field[current_position[0]][current_position[1]] = '-'
        current_position = [row, col]


if water_deposits_count >= 1 and metal_deposits_count >= 1 and concrete_deposits_count >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")