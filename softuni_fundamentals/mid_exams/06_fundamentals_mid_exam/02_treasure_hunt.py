from typing import List


def is_index_valid(loot: List[str], index: int):
    return 0 <= index < len(loot)


def print_stolen_items(loot: List[str]):
    print(', '.join(loot))


def final_result(loot: List[str]):
    if not loot:
        return 'Failed treasure hunt.'
    loot_sum = sum([len(el) for el in loot])
    return f'Average treasure gain: {loot_sum / len(loot):.2f} pirate credits.'


def process_commands(command: str, loot: List[str], *args):

    if command == 'Yohoho!':
        return True, loot

    if command == 'Loot':
        for arg in args:
            if arg not in loot:
                loot.insert(0, arg)

    elif command == 'Drop':
        index = int(args[0])
        if is_index_valid(loot, index):
            loot.append(loot.pop(index))

    elif command == 'Steal':
        count = int(args[0])
        if count >= len(loot):
            print_stolen_items(loot)
            loot.clear()
        else:
            stolen_items = loot[len(loot) - count:]
            loot = loot[:len(loot) - count]
            print_stolen_items(stolen_items)

    return False, loot


def main():
    loot = input().split('|')

    while True:
        command_args = input().split()

        command = command_args[0]
        args = command_args[1:]

        is_end, loot = process_commands(command, loot, *args)

        if is_end:
            break

    print(final_result(loot))


if __name__ == '__main__':
    main()
