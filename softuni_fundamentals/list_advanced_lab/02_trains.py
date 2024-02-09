from typing import List


def commands_executor(wagons: List[int], command, *args):
    if command == 'End':
        print(wagons)
        return True

    if command == 'add':
        wagons[-1] += args[0]
    elif command == 'insert':
        index, people = args
        wagons[index] += people
    elif command == 'leave':
        index, people = args
        wagons[index] -= people

    return False


def main():
    wagons = [0] * int(input())

    while True:
        command_args = input().split()
        command = command_args[0]
        args = list(map(int, command_args[1:]))
        is_end = commands_executor(wagons, command, *args)

        if is_end:
            break


if __name__ == '__main__':
    main()