WATER_TANK_CAPACITY = 255

num = int(input())
water_in_tank = 0

for _ in range(num):
    water_to_pour_in_tank = int(input())

    if water_in_tank + water_to_pour_in_tank <= WATER_TANK_CAPACITY:
        water_in_tank += water_to_pour_in_tank
    else:
        print('Insufficient capacity!')

print(water_in_tank)