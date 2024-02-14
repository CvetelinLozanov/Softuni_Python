from typing import List


def is_index_valid(ship: List[int], index: int):
    return 0 <= index < len(ship)


def are_pirate_ship_indexes_valid(ship: List[int], start_index: int, end_index: int):
    return 0 <= start_index <= len(ship) and 0 <= end_index + 1 <= len(ship)


def is_section_broken(ship: List[int], index):
    return ship[index] <= 0


def check_if_pirate_ship_is_sunken(pirate_ship: List[int], start_index: int, end_index: int, damage: int):
    for index in range(start_index, end_index + 1):
        pirate_ship[index] -= damage
        if is_section_broken(pirate_ship, index):
            return True


def main():
    pirate_ship = [int(el) for el in input().split('>')]
    war_ship = [int(el) for el in input().split('>')]
    max_health_capacity = int(input())

    while True:

        command_args = input().split()

        if command_args[0] == 'Retire':
            pirate_ship_sum = sum(pirate_ship)
            war_ship_sum = sum(war_ship)
            print(f'Pirate ship status: {pirate_ship_sum}\nWarship status: {war_ship_sum}')
            break

        if command_args[0] == 'Fire':
            index = int(command_args[1])
            damage = int(command_args[2])

            if is_index_valid(war_ship, index):
                war_ship[index] -= damage

                if is_section_broken(war_ship, index):
                    print('You won! The enemy ship has sunken.')
                    break

        elif command_args[0] == 'Defend':
            start_index = int(command_args[1])
            end_index = int(command_args[2])
            damage = int(command_args[3])
            if are_pirate_ship_indexes_valid(pirate_ship, start_index, end_index):
                is_sunken = check_if_pirate_ship_is_sunken(pirate_ship, start_index, end_index, damage)
                if is_sunken:
                    print('You lost! The pirate ship has sunken.')
                    break

        elif command_args[0] == 'Repair':
            index = int(command_args[1])
            health = int(command_args[2])
            if is_index_valid(pirate_ship, index):
                pirate_ship[index] += health
                if pirate_ship[index] > max_health_capacity:
                    pirate_ship[index] = max_health_capacity

        elif command_args[0] == 'Status':
            repair_boundary = max_health_capacity * 0.20
            sections_to_repair = sum(section < repair_boundary for section in pirate_ship)
            print(f'{sections_to_repair} sections need repair.')


if __name__ == '__main__':
    main()