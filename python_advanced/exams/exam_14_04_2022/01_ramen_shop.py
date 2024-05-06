from collections import deque


bowls = [int(bowl) for bowl in input().split(', ')]
customers = deque([int(customer) for customer in input().split(', ')])

while bowls and customers:
    current_bowls = bowls[-1]
    current_customer = customers[0]

    if current_bowls == current_customer:
        bowls.pop()
        customers.popleft()

    elif current_bowls > current_customer:
        bowls[-1] -= current_customer
        customers.popleft()

    else:
        customers[0] -= current_bowls
        bowls.pop()

if not customers:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(map(str, bowls))}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str, customers))}")
