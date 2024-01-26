def is_valid_index(list, index):
    return 0 <= index < len(list)


gifts = input().split()

while True:
    command_args = input()
    if command_args == 'No Money':
        break

    command = command_args.split()[0]

    if command == 'OutOfStock':
        gift = command_args.split()[1]
        if gift in gifts:
            for index in range(len(gifts)):
                if gifts[index] == gift:
                    gifts[index] = None

    elif command == 'Required':
        gift, index = command_args.split()[1:]
        if is_valid_index(gifts, int(index)):
            gifts[int(index)] = gift

    elif command == 'JustInCase':
        gift = command_args.split()[1]
        gifts[-1] = gift


print(' '.join([gift for gift in gifts if gift is not None]))

