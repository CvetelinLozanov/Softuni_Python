from math import floor

truck_capacity = float(input())

bag_counter = 0
command = input()
total_bag_volume = 0

while command != 'End':

    bag_volume = floor(float(command))

    if (bag_counter + 1) % 3 == 0:
        bag_volume *= 1.10

    if bag_volume > truck_capacity:
        print(f'No more space!')
        break

    bag_counter += 1
    truck_capacity -= bag_volume
    command = input()

else:
    print(f'Congratulations! All suitcases are loaded!')

print(f'Statistic: {bag_counter} suitcases loaded.')
