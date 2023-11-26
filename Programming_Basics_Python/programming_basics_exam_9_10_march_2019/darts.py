name_of_player = input()
starting_points = 301

successful_number_of_shots = 0
unsuccessful_number_of_shots = 0


def is_lower(current_points, points):
    return current_points - points < 0


while True:

    if starting_points == 0:
        print(f'{name_of_player} won the leg with {successful_number_of_shots} shots.')
        break

    command = input()

    if command == 'Retire':
        print(f'{name_of_player} retired after {unsuccessful_number_of_shots} unsuccessful shots.')
        break

    field = command
    points = int(input())

    if field == 'Single':

        if is_lower(starting_points, points):
            unsuccessful_number_of_shots += 1
            continue
        else:
            starting_points -= points
            successful_number_of_shots += 1

    elif field == 'Double':

        if is_lower(starting_points, points * 2):
            unsuccessful_number_of_shots += 1
            continue
        else:
            starting_points -= points * 2
            successful_number_of_shots += 1

    elif field == 'Triple':

        if is_lower(starting_points, points * 3):
            unsuccessful_number_of_shots += 1
            continue
        else:
            starting_points -= points * 3
            successful_number_of_shots += 1
