from modules.fibonacci_sequence.core.fibonacci_helpers import create_fibonacci_sequence, locate_number, print_numbers


def execution():
    command = input()
    fibonacci_numbers = []

    while command != 'Stop':
        number = int(command.split()[-1])
        if command.startswith('Create'):
            fibonacci_numbers = create_fibonacci_sequence(number)
            print_numbers(fibonacci_numbers)
        elif command.startswith('Locate'):
            print(locate_number(number, fibonacci_numbers))

        command = input()
