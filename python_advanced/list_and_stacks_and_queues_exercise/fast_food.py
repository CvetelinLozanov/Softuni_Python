from collections import deque


food_quantity = int(input())
orders = deque([int(num) for num in input().split()])


for index in range(len(orders)):
    current_order = int(orders[index])


print(max(orders))

while orders:
    current_order = int(orders[0])

    if current_order <= food_quantity:
        orders.popleft()
        food_quantity -= current_order

    else:
        break

if len(orders) == 0:
    print('Orders complete')

else:
    print(f"Orders left: {' '.join(map(str,orders))}")
