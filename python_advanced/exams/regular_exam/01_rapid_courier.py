from collections import deque

packages = deque([int(pack) for pack in input().split()])
couriers = deque([int(courier) for courier in input().split()])

total_weight = 0

while packages and couriers:
    curr_package = packages.pop()
    curr_courier = couriers.popleft()

    if curr_courier >= curr_package:

        if curr_courier > curr_package:
            curr_courier -= 2 * curr_package

            if curr_courier > 0:
                couriers.append(curr_courier)

        total_weight += curr_package

    else:
        curr_package -= curr_courier
        packages.append(curr_package)
        total_weight += curr_courier

print(f"Total weight: {total_weight} kg")

if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")

elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages:"
          f" {', '.join(map(str, packages))}")

elif couriers and not packages:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers))} but there are no more packages to deliver.")