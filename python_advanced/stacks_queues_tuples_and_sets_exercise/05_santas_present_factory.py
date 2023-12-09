from collections import deque

material_boxes = deque(int(x) for x in input().split())
magic_values = deque(int(x) for x in input().split())

presents = {
    'Doll': [150, 0],
    'Wooden train': [250, 0],
    'Teddy bear': [300, 0],
    'Bicycle': [400, 0],
}

is_crafted = False

while material_boxes and magic_values:

    if material_boxes[-1] == 0 or magic_values[0] == 0:
        if magic_values[0] == 0:
            magic_values.popleft()

        if material_boxes[-1] == 0:
            material_boxes.pop()
        continue

    total_magic_level = magic_values[0] * material_boxes[-1]

    if total_magic_level < 0:
        sum_magic = magic_values[0] + material_boxes[-1]
        magic_values.popleft()
        material_boxes.pop()
        material_boxes.append(sum_magic)
        continue

    elif total_magic_level not in [x for v in presents.values() for x in v] and total_magic_level > 0:
        magic_values.popleft()
        material_boxes[-1] += 15
        continue

    for present, magic_vals in presents.items():

        if presents[present][0] == total_magic_level:
            presents[present][1] += 1
            magic_values.popleft()
            material_boxes.pop()

if presents['Doll'][1] >= 1 and presents['Wooden train'][1] >= 1:
    is_crafted = True
elif presents['Teddy bear'][1] >= 1 and presents['Bicycle'][1] >= 1:
    is_crafted = True

print('The presents are crafted! Merry Christmas!' if is_crafted else 'No presents this Christmas!')
if material_boxes:
    material_boxes.reverse()
    print(f"Materials left: {', '.join([str(x) for x in material_boxes])}")
if magic_values:
    print(f"Magic left: {', '.join([str(x) for x in magic_values])}")

for present, values in sorted(presents.items()):
    if presents[present][1] >= 1:
        print(f"{present}: {presents[present][1]}")
