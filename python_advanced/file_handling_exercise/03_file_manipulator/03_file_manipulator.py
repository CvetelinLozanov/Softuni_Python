import os


def process_commands(command, *args):
    file_name = args[0]
    if command == 'Create':
        file = open(file_name, 'w').close()

    elif command == 'Add':
        content = args[1]
        with open(file_name, 'a') as f:
            f.writelines(content + "\n")

    elif command == 'Replace':
        old_string = args[1]
        new_string = args[2]

        try:
            with open(file_name, 'r+') as f:
                content = f.read()
                f.seek(0)
                f.truncate(0)
                f.write(content.replace(old_string, new_string))
        except FileNotFoundError:
            print("An error occurred")

    elif command == 'Delete':

        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")


while True:
    text = input()

    if text == 'End':
        break

    command, *args = text.split('-')

    process_commands(command, *args)
