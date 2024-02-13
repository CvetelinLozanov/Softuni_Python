from typing import List


def is_index_valid(targets: List[int], index_):
    return 0 <= index_ < len(targets)


def are_multiple_indexes_valid(targets: List[int], lower_index, higher_index):
    return 0 <= lower_index < len(targets) and 0 <= higher_index < len(targets)


def strike_elements(targets: List[int], start_index: int, end_index: int):
    targets = targets[:start_index] + targets[end_index + 1:]
    return targets


def targets_processing(command, targets, *args):

    if command == 'End':
        print('|'.join(map(str, targets)))
        return True, targets

    index = int(args[0])
    value = int(args[1])

    if command == 'Shoot':
        if is_index_valid(targets, index):
            targets[index] -= value

            if targets[index] <= 0:
                targets.pop(index)

    elif command == 'Add':
        if is_index_valid(targets, index):
            targets.insert(index, value)
        else:
            print('Invalid placement!')

    elif command == 'Strike':
        lower_index = index - value
        higher_index = index + value
        if not are_multiple_indexes_valid(targets, lower_index, higher_index):
            print('Strike missed!')
            return False, targets

        targets = strike_elements(targets, lower_index, higher_index)

    return False, targets


def moving_target_main_logic():
    moving_targets = list(map(int, input().split()))

    while True:
        command_args = input().split()
        command = command_args[0]
        args = command_args[1:]
        is_end, moving_targets = targets_processing(command, moving_targets, *args)
        if is_end:
            break


moving_target_main_logic()



# from typing import List
#
#
# def is_index_valid(targets: List[int], index_):
#     return 0 <= index_ < len(targets)
#
#
# def are_multiple_indexes_valid(targets: List[int], lower_index, higher_index):
#     return 0 <= lower_index < len(targets) and 0 <= higher_index < len(targets)
#
#
# def strike_elements(targets: List[int], start_index: int, end_index: int):
#     targets = targets[:start_index] + targets[end_index + 1:]
#     return targets
#
#
# def moving_target_main_logic():
#     moving_targets = list(map(int, input().split()))
#
#     while True:
#         command_args = input().split()
#
#         if command_args[0] == 'End':
#             print('|'.join(map(str, moving_targets)))
#             break
#
#         index = int(command_args[1])
#         value = int(command_args[2])
#
#         if command_args[0] == 'Shoot':
#             if is_index_valid(moving_targets, index):
#                 moving_targets[index] -= value
#
#                 if moving_targets[index] <= 0:
#                     moving_targets.pop(index)
#
#         elif command_args[0] == 'Add':
#             if is_index_valid(moving_targets, index):
#                 moving_targets.insert(index, value)
#             else:
#                 print('Invalid placement!')
#
#         elif command_args[0] == 'Strike':
#             lower_index = index - value
#             higher_index = index + value
#             if not are_multiple_indexes_valid(moving_targets, lower_index, higher_index):
#                 print('Strike missed!')
#                 continue
#
#             moving_targets = strike_elements(moving_targets, lower_index, higher_index)
#
#
# moving_target_main_logic()