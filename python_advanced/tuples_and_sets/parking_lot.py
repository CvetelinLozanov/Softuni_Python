n = int(input())

cars = set()

for _ in range(n):
    destination, car_plate = input().split(', ')

    if destination == 'IN':
        cars.add(car_plate)

    elif destination == 'OUT':
        if car_plate in cars:
            cars.remove(car_plate)


if cars:
    [print(plate) for plate in cars]
else:
    print('Parking Lot is Empty')