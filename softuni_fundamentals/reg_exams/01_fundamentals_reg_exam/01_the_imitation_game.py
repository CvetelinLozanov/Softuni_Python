from typing import List


def process_commands(message: str):
    while True:
        text = input()

        if text == 'Decode':
            return message

        command_args = text.split('|')

        if command_args[0] == 'ChangeAll':
            substring_to_replace = command_args[1]
            new_string = command_args[2]
            message = message.replace(substring_to_replace, new_string)

        elif command_args[0] == 'Insert':
            index = int(command_args[1])
            value = command_args[2]
            message = list(message)
            message.insert(index, value)
            message = ''.join(message)

        elif command_args[0] == 'Move':
            number_of_letters = int(command_args[1])
            text_to_move = message[:number_of_letters]
            message = message[number_of_letters:] + text_to_move


encrypted_message = input()
encrypted_message = process_commands(encrypted_message)
print(f'The decrypted message is: {encrypted_message}')