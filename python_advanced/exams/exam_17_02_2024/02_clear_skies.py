def is_index_valid(row, col, field_length):
    return 0 <= row < field_length and 0 <= col < field_length


def fill_field(n):
    current_position_ = []
    field_ = []
    enemies_counter_ = 0
    for row in range(n):
        field_.append(list(input()))
        for col in range(n):
            if field_[row][col] == 'J':
                current_position_ = [row, col]
            elif field_[row][col] == 'E':
                enemies_counter_ += 1

    return current_position_, field_, enemies_counter_


n = int(input())
directions = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}
current_position, field, enemies_counter = fill_field(n)

initial_jet_armour = 300

while initial_jet_armour > 0:
    command = input()

    if command in directions:
        row, col = current_position[0] + directions[command][0], current_position[1] + directions[command][1]

        if field[row][col] == 'R' and is_index_valid(row, col, n):
            initial_jet_armour = 300

        elif field[row][col] == 'E' and is_index_valid(row, col, n):
            enemies_counter -= 1
            if enemies_counter > 0:
                initial_jet_armour -= 100

        field[current_position[0]][current_position[1]] = '-'
        field[row][col] = 'J'
        current_position = [row, col]

        if enemies_counter == 0:
            print('Mission accomplished, you neutralized the aerial threat!')
            break

if initial_jet_armour <= 0 < enemies_counter:
    print(f'Mission failed, your jetfighter was shot down! Last coordinates {current_position}!')

[print(''.join(row)) for row in field]