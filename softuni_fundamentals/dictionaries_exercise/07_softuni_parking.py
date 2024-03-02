n = int(input())

parking = {}

for _ in range(n):
    command_args = input().split()

    if len(command_args) == 3:
        username, reg_plate = command_args[1:]

        if username not in parking:
            parking[username] = reg_plate
            print(f'{username} registered {reg_plate} successfully')
        else:
            print(f'ERROR: already registered with plate number {reg_plate}')

    else:
        username = command_args[1]
        if username in parking:
            del parking[username]
            print(f'{username} unregistered successfully')
        else:
            print(f'ERROR: user {username} not found')


[print(f'{user} => {reg_plate}') for user, reg_plate in parking.items()]