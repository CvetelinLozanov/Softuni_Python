from collections import deque

number_of_petrol_stations = int(input())
petrol_info = deque()
counter = 0
total_fuel = 0
is_fuel_enough = False

for i in range(number_of_petrol_stations):
    petrol_info.append([int(x) for x in input().split()])

while True:

    for args in petrol_info:
        fuel = int(args[0])
        distance = int(args[1])
        total_fuel += fuel

        if total_fuel < distance:
            is_fuel_enough = False
            break

        else:
            total_fuel -= distance
            is_fuel_enough = True

    if is_fuel_enough:
        break

    petrol_info.rotate(-1)
    total_fuel = 0
    counter += 1

print(counter)
