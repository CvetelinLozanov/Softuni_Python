def is_valid_index(text_, index):
    return 0 <= index < len(text_)


def process_commands(stops: str, text_: str):
    if text_ == 'Travel':
        print(f'Ready for world tour! Planned stops: {stops}')
        return True, stops

    command_args = text_.split(':')

    if command_args[0] == 'Add Stop':
        index, stop = command_args[1:]
        index = int(index)
        if is_valid_index(stops, index):
            stops = list(stops)
            stops.insert(index, stop)
            stops = ''.join(stops)

    elif command_args[0] == 'Remove Stop':
        start_index = int(command_args[1])
        end_index = int(command_args[2])

        if is_valid_index(stops, start_index) and is_valid_index(stops, end_index):
            stops = stops[:start_index] + stops[end_index + 1:]

    elif command_args[0] == 'Switch':
        old_string, new_string = command_args[1:]

        if old_string in stops:
            stops = stops.replace(old_string, new_string)

    print(stops)

    return False, stops


def main():
    stops = input()
    while True:
        text = input()

        is_end, stops = process_commands(stops, text)

        if is_end:
            break


if __name__ == '__main__':
    main()
