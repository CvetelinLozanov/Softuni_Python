from collections import deque


customers = deque([int(customer) for customer in input().split(', ')])
taxis = deque([int(taxi) for taxi in input().split(', ')])
total_time = 0

while customers and taxis:
    current_customer = customers[0]
    current_taxi = taxis[-1]

    if current_taxi >= current_customer:
        total_time += current_customer
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()


if not customers:
    print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")
else:
    print(f"Not all customers were driven to their destinations\nCustomers left: {', '.join(map(str, customers))}")
