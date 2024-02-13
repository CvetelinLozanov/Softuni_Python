from typing import List


def process_groceries(command: str, groceries: List[str], *args):

    if command == 'Go':
        print(', '.join(groceries))
        return True

    if command == 'Urgent':
        item = args[0]
        if item in groceries:
            return False
        groceries.insert(0, item)

    elif command == 'Unnecessary':
        item = args[0]
        if item in groceries:
            groceries.remove(item)

    elif command == 'Correct':
        old_item, new_item = args

        if old_item in groceries:
            index_of_old_item = groceries.index(old_item)
            groceries[index_of_old_item] = new_item

    elif command == 'Rearrange':
        item = args[0]

        if item in groceries:
            index_of_item = groceries.index(item)
            current_item = groceries.pop(index_of_item)
            groceries.append(current_item)


def shopping_list_logic():
    groceries = input().split('!')

    while True:

        command_args = input().split()

        command = command_args[0]
        args = command_args[1:]

        is_end = process_groceries(command, groceries, *args)

        if is_end:
            break


shopping_list_logic()