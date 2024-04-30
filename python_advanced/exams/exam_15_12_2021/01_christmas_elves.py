from collections import deque


elves = deque([int(elf) for elf in input().split()])
materials = deque([int(box) for box in input().split()])
toys = 0
counter = 1
used_energy = 0

while elves and materials:
    current_elf = elves[0]
    current_material = materials[-1]

    if current_elf < 5:
        elves.popleft()
        continue

    toys_to_be_created = 1
    energy_increase = 1

    if counter % 3 == 0:
        current_material *= 2
        toys_to_be_created = 2

    if counter % 5 == 0:
        toys_to_be_created = 0
        energy_increase = 0

    if current_elf >= current_material:
        toys += toys_to_be_created
        used_energy += current_material
        elves[0] -= current_material
        elves[0] += energy_increase
        elves.rotate(-1)
        materials.pop()

    else:
        elves[0] *= 2
        elves.rotate(-1)

    counter += 1

print(f"Toys: {toys}")
print(f"Energy: {used_energy}")

if elves:
    print(f"Elves left: {', '.join(map(str, elves))}")
if materials:
    print(f"Boxes left: {', '.join(map(str, materials))}")



# elves = deque([int(elf) for elf in input().split()])
# materials = deque([int(box) for box in input().split()])
# toys = 0
# counter = 1
# used_energy = 0
#
# while elves and materials:
#     current_elf = elves[0]
#     current_material = materials[-1]
#
#     if current_elf < 5:
#         elves.popleft()
#         continue
#
#     factor = 1
#
#     if counter % 3 == 0:
#         current_material *= 2
#
#     if current_elf >= current_material:
#         toys += 1
#         if counter % 3 == 0:
#             toys += 1
#         if counter % 5 == 0:
#             toys -= 1
#             factor = 0
#         if counter % 15 == 0:
#             toys -= 1
#             factor = 0
#         used_energy += current_material
#         elves[0] -= current_material
#         elves[0] += factor
#         elves.rotate(-1)
#         materials.pop()
#     else:
#         elves[0] *= 2
#         elves.rotate(-1)
#
#     counter += 1
#
# print(f"Toys: {toys}")
# print(f"Energy: {used_energy}")
#
# if elves:
#     print(f"Elves left: {', '.join(map(str, elves))}")
# if materials:
#     print(f"Boxes left: {', '.join(map(str, materials))}")