import math

type_of_figure = input()

if type_of_figure == 'square':
    side_length = float(input())
    area_of_square = side_length * side_length
    print(f"{area_of_square:.3f}")
elif type_of_figure == 'rectangle':
    side_a_length = float(input())
    side_b_length = float(input())
    area_of_rectangle = side_a_length * side_b_length
    print(f"{area_of_rectangle:.3f}")
elif type_of_figure == 'circle':
    radius = float(input())
    area_of_circle = math.pi * math.pow(radius,2)
    print(f"{area_of_circle:.3f}")
elif type_of_figure == 'triangle':
    side_length = float(input())
    height_length = float(input())
    area_of_triangle = (side_length * height_length) / 2
    print(f"{area_of_triangle}")

