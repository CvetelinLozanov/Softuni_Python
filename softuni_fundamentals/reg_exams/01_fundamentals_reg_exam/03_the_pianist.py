from typing import Dict


def fill_pieces(n: int):
    pieces = {}
    for _ in range(n):
        piece, composer, key = input().split('|')
        if piece not in pieces:
            pieces[piece] = {}

        pieces[piece]['key'] = key
        pieces[piece]['composer'] = composer

    return pieces


def process_commands(pieces: Dict[str, Dict[str, str]]):
    while True:
        text = input()

        if text == 'Stop':
            return pieces

        command_args = text.split('|')

        if command_args[0] == 'Add':
            piece, composer, key = command_args[1:]
            if piece in pieces:
                print(f'{piece} is already in the collection!')
            else:
                pieces[piece] = {}
                pieces[piece]['key'] = key
                pieces[piece]['composer'] = composer
                print(f'{piece} by {composer} in {key} added to the collection!')

        elif command_args[0] == 'Remove':
            piece = command_args[1]
            if piece in pieces:
                del pieces[piece]
                print(f'Successfully removed {piece}!')
            else:
                print(f'Invalid operation! {piece} does not exist in the collection.')

        elif command_args[0] == 'ChangeKey':
            piece, key = command_args[1:]
            if piece in pieces:
                pieces[piece]['key'] = key
                print(f'Changed the key of {piece} to {key}!')
            else:
                print(f'Invalid operation! {piece} does not exist in the collection.')


def print_pieces(pieces: Dict[str, Dict[str, str]]):
    for piece, piece_info in pieces.items():
        composer = piece_info['composer']
        key = piece_info['key']
        print(f'{piece} -> Composer: {composer}, Key: {key}')


def main():
    n = int(input())
    pieces = fill_pieces(n)
    pieces = process_commands(pieces)
    print_pieces(pieces)


if __name__ == '__main__':
    main()