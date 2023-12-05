from collections import deque

box_with_clothes = deque([int(x) for x in input().split()])
rack_capacity = int(input())
racks_counter = 0
clothes_sum = 0

while box_with_clothes:
    racks_counter += 1
    current_rack_capacity = rack_capacity

    while box_with_clothes and box_with_clothes[-1] <= current_rack_capacity:
        current_rack_capacity -= box_with_clothes.pop()

print(racks_counter)

