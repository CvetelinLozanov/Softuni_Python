def take_odd(password_: str):
    new_pass = ''.join([ch for index, ch in enumerate(password_) if index % 2 != 0])
    return new_pass


def cut_password(password_: str, index_: int, length_: int):
    sub_pass = password_[index_: index_ + length_]
    return password_.replace(sub_pass, '', 1)


def substitute_password(password_: str, substring_: str, substitute_: str):
    is_find = False
    if substring_ in password_:
        password_ = password_.replace(substring_, substitute_)
        is_find = True
        return password_, is_find
    return password_, is_find


password = input()

while True:
    text = input()

    if text == 'Done':
        break

    command_args = text.split()

    if command_args[0] == 'TakeOdd':
        password = take_odd(password)
        print(password)

    elif command_args[0] == 'Cut':
        index = int(command_args[1])
        length = int(command_args[2])
        password = cut_password(password, index, length)
        print(password)

    elif command_args[0] == 'Substitute':
        substring = command_args[1]
        substitute = command_args[2]
        password, is_find = substitute_password(password, substring, substitute)
        if not is_find:
            print('Nothing to replace!')
        else:
            print(password)

print(f'Your password is: {password}')
