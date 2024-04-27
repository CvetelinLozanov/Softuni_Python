from collections import deque


pizza_orders = deque([int(pizza) for pizza in input().split(', ')])
pizza_makers = deque([int(maker) for maker in input().split(', ')])
pizza_count = 0


while pizza_orders and pizza_makers:

    if pizza_orders[0] <= 0 or pizza_orders[0] > 10:
        pizza_orders.popleft()
        continue

    current_pizza = pizza_orders[0]
    current_maker = pizza_makers[-1]

    if current_pizza <= current_maker:
        pizza_makers.pop()
        pizza_orders.popleft()
        pizza_count += current_pizza
    else:
        pizza_orders[0] -= current_maker
        pizza_makers.pop()
        pizza_count += current_maker

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizza_count}")
    print(f"Employees: {', '.join(map(str, pizza_makers))}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, pizza_orders))}")
