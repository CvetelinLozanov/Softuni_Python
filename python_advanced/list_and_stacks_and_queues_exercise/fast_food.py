from collections import deque
from sys import  maxsize


def check_max_value_in_stack(max_value, value):
    return max_value < value


food_quantity = int(input())
quantity_of_food_per_client = deque(input().split())
biggest_order = -maxsize

for index in range(len(quantity_of_food_per_client)):
    current_order = int(quantity_of_food_per_client[index])

    if check_max_value_in_stack(biggest_order, current_order):
        biggest_order = current_order

print(biggest_order)

while len(quantity_of_food_per_client) != 0:
    current_order = int(quantity_of_food_per_client[0])

    if current_order <= food_quantity:
        quantity_of_food_per_client.popleft()
        food_quantity -= current_order

    else:
        break

if len(quantity_of_food_per_client) == 0:
    print('Orders complete')

else:
    print('Orders left: ', end='')
    while quantity_of_food_per_client:
        print(quantity_of_food_per_client.popleft(), end='')
        if quantity_of_food_per_client:
            print(', ', end='')
