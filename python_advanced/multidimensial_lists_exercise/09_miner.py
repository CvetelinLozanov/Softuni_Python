from collections import deque


def get_start_position(field):
    start_row = None
    start_col = None
    is_start_find = False
    for row in range(len(field)):
        for col in range(len(field)):

            if field[row][col] == 's':
                start_row = row
                start_col = col
                is_start_find = True
                break

        if is_start_find:
            break

    return start_row, start_col


def is_valid(field, row, col):
    return 0 <= row < len(field) and 0 <= col < len(field)


def is_end(field, row, col):
    return field[row][col].lower() == 'e'


def is_coal(field, row, col):
    return field[row][col].lower() == 'c'


def print_end():
    print(f"Game over! ({start_row}, {start_col})")


def are_remaining_coal(field):
    return len([el for x in field for el in x if el == 'c']) > 0


n = int(input())
commands = deque(input().split())
game_field = [[x for x in input().split()] for _ in range(n)]
coal_counter = 0
start_row, start_col = get_start_position(game_field)
is_finished = False

while commands:
    command_movement = commands.popleft()

    if (command_movement == 'right' and is_valid(game_field, start_row, start_col + 1)) or ((command_movement == 'left' and is_valid(game_field, start_row, start_col - 1)))\
            or ((command_movement == 'up' and is_valid(game_field, start_row - 1, start_col))) or ((command_movement == 'down' and is_valid(game_field, start_row + 1, start_col))):

        if command_movement.lower() == 'up':
            start_row -= 1

            if is_end(game_field, start_row, start_col):
                print_end()
                is_finished = True

            elif is_coal(game_field, start_row, start_col):
                coal_counter += 1
                game_field[start_row][start_col] = '*'

        elif command_movement.lower() == 'down':
            start_row += 1

            if is_end(game_field, start_row, start_col):
                print_end()
                is_finished = True

            elif is_coal(game_field, start_row, start_col):
                coal_counter += 1
                game_field[start_row][start_col] = '*'

        elif command_movement.lower() == 'right':
            start_col += 1

            if is_end(game_field, start_row, start_col):
                print_end()
                is_finished = True

            elif is_coal(game_field, start_row, start_col):
                coal_counter += 1
                game_field[start_row][start_col] = '*'

        elif command_movement.lower() == 'left':
            start_col -= 1

            if is_end(game_field, start_row, start_col):
                print_end()
                is_finished = True

            elif is_coal(game_field, start_row, start_col):
                coal_counter += 1
                game_field[start_row][start_col] = '*'
    else:
        continue

    if not are_remaining_coal(game_field):
        print(f'You collected all coal! ({start_row}, {start_col})')
        is_finished = True


if not is_finished:
    remaining_field_with_coal = [el for x in game_field for el in x if el == 'c']
    print(f'{len(remaining_field_with_coal)} pieces of coal left. ({start_row}, {start_col})')
