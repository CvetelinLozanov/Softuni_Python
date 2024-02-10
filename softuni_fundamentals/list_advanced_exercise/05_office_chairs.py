def check_office_chairs():
    number_of_rooms = int(input())
    free_chairs, are_enough_chairs = are_chairs_enough(number_of_rooms)
    if are_enough_chairs:
        print(f'Game On, {free_chairs} free chairs left')


def are_chairs_enough(number_of_rooms: int):
    free_chairs = 0
    are_enough_chairs = True
    for room in range(number_of_rooms):
        chairs, visitors = input().split()
        visitors = int(visitors)

        if len(chairs) >= visitors:
            free_chairs += len(chairs) - visitors
        else:
            print(f'{visitors - len(chairs)} more chairs needed in room {room + 1}')
            are_enough_chairs = False

    return free_chairs, are_enough_chairs


check_office_chairs()
