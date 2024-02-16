from typing import List


def process_commands(items: List[str], command: str, *args):

    if command == 'Craft!':
        return items, True
    elif command == 'Collect':
        item = args[0]
        if item not in items:
            items.append(item)

    elif command == 'Drop':
        item = args[0]
        if item in items:
            items.remove(item)

    elif command == 'Combine Items':
        old_item, new_item = args[0].split(':')
        if old_item in items:
            old_item_index = items.index(old_item)
            items.insert(old_item_index + 1, new_item)

    elif command == 'Renew':
        item = args[0]
        if item in items:
            items.remove(item)
            items.append(item)

    return items, False


def main():
    items = input().split(', ')

    while True:
        command_args = input().split(' - ')
        command = command_args[0]
        args = command_args[1:]
        items, is_end = process_commands(items, command, *args)

        if is_end:
            break

    print(', '.join(items))


if __name__ == '__main__':
    main()
