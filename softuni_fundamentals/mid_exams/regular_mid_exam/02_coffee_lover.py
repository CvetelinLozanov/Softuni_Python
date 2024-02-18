def check_if_index_is_valid(coffee, index):
    return 0 <= index < len(coffee)


def process_commands(coffee, number_of_commands: int):
    for _ in range(number_of_commands):
        command_args = input().split()

        if command_args[0] == 'Include':
            item = command_args[1]
            coffee.append(item)

        elif command_args[0] == 'Remove':
            sub_command = command_args[1]
            items_to_remove = int(command_args[2])
            if sub_command == 'first':
                if len(coffee) > items_to_remove:
                    coffee = coffee[items_to_remove:]
                else:
                    coffee.clear()
            elif sub_command == 'last':
                if len(coffee) > items_to_remove:
                    coffee = coffee[:len(coffee) - items_to_remove]
                else:
                    coffee.clear()

        elif command_args[0] == 'Prefer':
            first_index = int(command_args[1])
            second_index = int(command_args[2])
            if check_if_index_is_valid(coffee, first_index) and check_if_index_is_valid(coffee, second_index):
                coffee[first_index], coffee[second_index] = coffee[second_index], coffee[first_index]

        elif command_args[0] == 'Reverse':
            coffee.reverse()

    return coffee


def print_coffees(coffee):
    return f'Coffees:\n{" ".join(coffee)}'


def main():
    coffee = input().split()
    number_of_commands = int(input())

    coffee = process_commands(coffee, number_of_commands)
    print(print_coffees(coffee))


if __name__ == '__main__':
    main()
