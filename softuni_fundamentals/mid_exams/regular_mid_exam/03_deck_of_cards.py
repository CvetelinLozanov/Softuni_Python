from typing import List


def check_if_index_is_valid(cards: List[str], index: int):
    return 0 <= index < len(cards)


def process_commands(cards: List[str], command: str, *args):
    if command == 'Add':
        card = args[0]
        if card not in cards:
            cards.append(card)
            print('Card successfully added')
        else:
            print('Card is already in the deck')

    elif command == 'Remove':
        card = args[0]
        if card not in cards:
            print('Card not found')
        else:
            cards.remove(card)
            print('Card successfully removed')

    elif command == 'Remove At':
        index = int(args[0])
        if check_if_index_is_valid(cards, index):
            cards.pop(index)
            print('Card successfully removed')
        else:
            print('Index out of range')

    elif command == 'Insert':
        index = int(args[0])
        card = args[1]
        if not check_if_index_is_valid(cards, index):
            print('Index out of range')
        else:
            if card in cards:
                print('Card is already added')
            else:
                cards.insert(index, card)
                print('Card successfully added')


def print_cards(cards: List[str]):
    return ', '.join(cards)


def process_cards(cards: List[str], number_of_commands: int):
    for _ in range(number_of_commands):
        command_args = input().split(', ')
        command = command_args[0]
        args = command_args[1:]
        process_commands(cards, command, *args)

    return cards


def main():
    cards = input().split(', ')
    number_of_commands = int(input())

    cards = process_cards(cards, number_of_commands)

    print(print_cards(cards))


if __name__ == '__main__':
    main()