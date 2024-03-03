def check_if_user_in_force_book(force_book, force_user):
    force_side = ''
    for force_side, users in force_book.items():
        if force_user in users:
            return True, force_side

    return False, force_side


def process_forces(force_book, force_side, force_user):
    if force_side not in force_book:
        force_book[force_side] = []

    is_exists, current_force_side = check_if_user_in_force_book(force_book, force_user)
    if not is_exists:
        force_book[force_side].append(force_user)


def process_change_force_side(force_book, force_user, force_side):
    is_exists, current_force_side = check_if_user_in_force_book(force_book, force_user)
    if is_exists:
        if current_force_side != force_side:
            force_book[current_force_side].remove(force_user)

    if force_side not in force_book:
        force_book[force_side] = []

    force_book[force_side].append(force_user)

    print(f'{force_user} joins the {force_side} side!')


def print_forces(force_book):
    for force_side, users in force_book.items():
        if len(users) > 0:
            print(f'Side: {force_side}, Members: {len(users)}')
            for user in users:
                print(f'! {user}')


force_book = {}
while True:

    command = input()
    delimiter = ''

    if command == 'Lumpawaroo':
        break

    if '|' in command:
        force_side, force_user = command.split(' | ')
        process_forces(force_book, force_side, force_user)
    else:
        force_user, force_side = command.split(' -> ')
        process_change_force_side(force_book, force_user, force_side)


print_forces(force_book)
