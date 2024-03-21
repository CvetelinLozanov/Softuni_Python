def process_commands(command: str, concealed_message_: str, *args):
    is_error = False
    if command == 'InsertSpace':
        index = int(args[0])
        concealed_message_ = list(concealed_message_)
        concealed_message_.insert(index, ' ')
        concealed_message_ = ''.join(concealed_message_)

    elif command == 'Reverse':
        substring = args[0]
        if substring in concealed_message_:
            start_index = concealed_message_.index(substring)
            end_index = start_index + len(substring)
            cut_word = concealed_message_[start_index:end_index]
            concealed_message_ = concealed_message_[:start_index] + concealed_message_[end_index:] + cut_word[::-1]
        else:
            print('error')
            is_error = True

    elif command == 'ChangeAll':
        substring = args[0]
        replacement = args[1]
        concealed_message_ = concealed_message_.replace(substring, replacement)

    return concealed_message_, is_error


concealed_message = input()

while True:
    text = input()

    if text == 'Reveal':
        break

    command, *args = text.split(':|:')

    concealed_message, is_error = process_commands(command, concealed_message, *args)
    if not is_error:
        print(concealed_message)

print(f'You have a new text message: {concealed_message}')