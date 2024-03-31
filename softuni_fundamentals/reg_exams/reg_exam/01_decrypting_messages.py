def is_valid_index(text_: str, index: int):
    return 0 <= index < len(text_)


def replace(text_:str, current_char: str, new_char: str):
    return text_.replace(current_char, new_char)


def calculate_ascii_sum(text_: str, start_index_: int, end_index_: int):
    chars_sum = 0

    for index in range(start_index_, end_index_ + 1):
        chars_sum += ord(text_[index])

    return chars_sum

text_to_decrypt = input()

while True:
    text = input()

    if text == 'Finish':
        break

    command_args = text.split()

    if command_args[0] == 'Replace':
        current_char = command_args[1]
        new_char = command_args[2]
        text_to_decrypt = replace(text_to_decrypt, current_char, new_char)
        print(text_to_decrypt)

    elif command_args[0] == 'Cut':
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        if is_valid_index(text_to_decrypt, start_index) and is_valid_index(text_to_decrypt, end_index):
            cut_string = text_to_decrypt[:start_index] + text_to_decrypt[end_index + 1:]
            text_to_decrypt = cut_string
            print(text_to_decrypt)
        else:
            print('Invalid indices!')

    elif command_args[0] == 'Make':
        sub_command = command_args[1]
        if sub_command == 'Upper':
            text_to_decrypt = text_to_decrypt.upper()
        elif sub_command == 'Lower':
            text_to_decrypt = text_to_decrypt.lower()

        print(text_to_decrypt)

    elif command_args[0] == 'Check':
        string_to_check = command_args[1]

        if string_to_check in text_to_decrypt:
            print(f'Message contains {string_to_check}')
        else:
            print(f"Message doesn't contain {string_to_check}")

    elif command_args[0] == 'Sum':
        start_index = int(command_args[1])
        end_index = int(command_args[2])

        if is_valid_index(text_to_decrypt, start_index) and is_valid_index(text_to_decrypt, end_index):
            sum_of_chars = calculate_ascii_sum(text_to_decrypt, start_index, end_index)
            print(sum_of_chars)

        else:
            print("Invalid indices!")