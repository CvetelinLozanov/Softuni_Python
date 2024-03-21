def is_index_valid(index, word):
    return 0 <= index < len(word)


def process_commands(command: str, username_: str, *args):
    if command == 'Letters':
        sub_command = args[0]
        if sub_command == 'Lower':
            username_ = username_.lower()
        elif sub_command == 'Upper':
            username_ = username_.upper()

        print(username_)

    elif command == 'Reverse':
        start_index = int(args[0])
        end_index = int(args[1])
        if is_index_valid(start_index, username_) and is_index_valid(end_index, username_):
            middle_word = username_[start_index:end_index + 1]
            print(middle_word[::-1])

    elif command == 'Substring':
        substring = args[0]
        if substring in username_:
            username_ = username_.replace(substring, '')
            print(username_)
        else:
            print(f"The username {username_} doesn't contain {substring}.")

    elif command == 'Replace':
        chars_to_replace = args[0]
        username_ = username_.replace(chars_to_replace, '-')
        print(username_)

    elif command == 'IsValid':
        char = args[0]
        if char in username_:
            print('Valid username.')
        else:
            print(f'{char} must be contained in your username.')

    return username_


username = input()

while True:
    command, *args = input().split()

    if command == 'Registration':
        break

    username = process_commands(command, username, *args)