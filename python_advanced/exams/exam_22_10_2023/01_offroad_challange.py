from collections import deque


initial_fuels = deque([int(num) for num in input().split()])
consumption_indexes = deque([int(num) for num in input().split()])
fuel_needed = deque([int(num) for num in input().split()])
altitude_count = 0
altitudes = []

while initial_fuels and consumption_indexes and fuel_needed:
    current_fuel = initial_fuels.pop()
    current_consumption_index = consumption_indexes.popleft()
    current_fuel_needed = fuel_needed.popleft()

    calculation = current_fuel - current_consumption_index

    if calculation >= current_fuel_needed:
        altitude_count += 1
        altitudes.append(f"Altitude {altitude_count}")
        print(f"John has reached: Altitude {altitude_count}")
    else:
        altitude_count += 1
        print(f"John did not reach: Altitude {altitude_count}")
        break

if len(altitudes) == 4:
    print("John has reached all the altitudes and managed to reach the top!")
else:
    print("John failed to reach the top.")
    if altitudes:
        print(f"Reached altitudes: {', '.join(altitudes)}")
    else:
        print("John didn't reach any altitude.")

