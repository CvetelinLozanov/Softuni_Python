from collections import deque


def accommodate_new_pets(*args):
    hotel_capacity = int(args[0])
    max_weight = float(args[1])
    accommodated_pets = {}
    pets = deque(args[2:])
    result = []
    while pets:

        pet_type = pets[0][0]
        pet_weight = float(pets[0][1])

        if hotel_capacity == 0:
            break

        if pet_weight > max_weight:
            pets.popleft()
            continue

        if pet_type not in accommodated_pets:
            accommodated_pets[pet_type] = []

        accommodated_pets[pet_type].append(pet_weight)
        hotel_capacity -= 1
        pets.popleft()

    sorted_pets = sorted(accommodated_pets.items(), key=lambda x: x[0])

    if not pets:
        result.append(f'All pets are accommodated! Available capacity: {hotel_capacity}.')
    else:
        result.append('You did not manage to accommodate all pets!')

    result.append('Accommodated pets:')

    [result.append(f'{key}: {len(value)}') for key, value in sorted_pets]

    return '\n'.join(result)


print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))