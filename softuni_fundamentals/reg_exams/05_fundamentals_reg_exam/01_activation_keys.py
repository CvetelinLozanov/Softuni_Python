activation_key = input()

while True:
    text = input()
    if text == 'Generate':
        break

    command_args = text.split('>>>')

    if command_args[0] == 'Contains':
        string_to_check = command_args[1]

        if string_to_check in activation_key:
            print(f'{activation_key} contains {string_to_check}')
        else:
            print('Substring not found!')

    elif command_args[0] == 'Flip':
        sub_command = command_args[1]
        start_index = int(command_args[2])
        end_index = int(command_args[3])
        if sub_command == 'Upper':
            activation_key = (activation_key[:start_index] + activation_key[start_index:end_index].upper()
                              + activation_key[end_index:])
        elif sub_command == 'Lower':
            activation_key = (activation_key[:start_index] + activation_key[start_index:end_index].lower()
                              + activation_key[end_index:])
        print(activation_key)

    elif command_args[0] == 'Slice':
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

print(f'Your activation key is: {activation_key}')