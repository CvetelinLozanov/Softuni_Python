from collections import deque


def best_list_pureness(*args):
    list = deque(args[0])
    rotate_times = args[1]
    best_rotation, best_sum = 0, 0
    for rotation in range(rotate_times + 1):
        shuffle_sum = sum([index * list[index] for index in range(len(list))])
        if shuffle_sum > best_sum:
            best_rotation = rotation
            best_sum = shuffle_sum
        list.rotate()

    return f"Best pureness {best_sum} after {best_rotation} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)