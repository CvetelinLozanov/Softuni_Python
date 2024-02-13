from typing import List


def is_valid_index(targets_: List[int], index_: int):
    return 0 <= index_ < len(targets_) and targets_[index_] != -1


def increase_and_decrease_targets(targets: List[int], current_target: int):
    for index in range(len(targets)):
        if targets[index] == -1:
            continue

        if targets[index] > current_target:
            targets[index] -= current_target

        else:
            targets[index] += current_target


def shoot_for_the_win_main_logic():
    targets = list(map(int, input().split()))
    shot_targets_count = 0

    while True:
        command = input()

        if command == 'End':
            print(f'Shot targets: {shot_targets_count} -> {" ".join(map(str, targets))}')
            break

        index = int(command)

        if is_valid_index(targets, index):
            current_target = targets[index]
            targets[index] = -1
            increase_and_decrease_targets(targets, current_target)
            shot_targets_count += 1


shoot_for_the_win_main_logic()
