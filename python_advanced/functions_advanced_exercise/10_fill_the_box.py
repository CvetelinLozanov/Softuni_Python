from collections import deque


def fill_the_box(*args):
    numbers = deque(args)
    height = numbers.popleft()
    length = numbers.popleft()
    width = numbers.popleft()
    volume = height * length * width
    cubes_volume = 0
    while True:
        txt = numbers.popleft()
        if txt == 'Finish':
            break

        if volume >= txt:
            volume -= txt
        else:
            cubes_volume -= txt - volume
            volume = 0

    if volume > 0:
        return f'There is free space in the box. You could put {volume} more cubes.'
    else:
        return f'No more free space! You have {abs(cubes_volume)} more cubes.'



print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))