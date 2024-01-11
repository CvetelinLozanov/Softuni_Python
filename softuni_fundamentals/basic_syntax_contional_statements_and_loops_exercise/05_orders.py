n = int(input())

total_costs = 0

for _ in range(n):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())

    if (price_per_capsule < 0.01 or price_per_capsule > 100) or (days < 1 or days > 31) or (capsules < 1 or capsules > 2000):
        continue

    coffee_price = capsules * days * price_per_capsule
    print(f'The price for the coffee is: ${coffee_price:.2f}')
    total_costs += coffee_price

print(f'Total: ${total_costs:.2f}')
