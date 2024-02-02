from math import floor


def get_closest_coordinates(x1:float, y1: float, x2: float, y2: float):
    first_coordinates_sum = abs(x1) + abs(y1)
    second_coordinates_sum = abs(x2) + abs(y2)
    result = ''
    if first_coordinates_sum == second_coordinates_sum:
        result = f'({floor(x1)}, {floor(y1)})'
    elif first_coordinates_sum < second_coordinates_sum:
        result = f'({floor(x1)}, {floor(y1)})'
    else:
        result = f'({floor(x2)}, {floor(y2)})'

    return result


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(get_closest_coordinates(x1, y1, x2, y2))
