products = {}

while True:
    command = input()

    if command == 'statistics':
        break

    product, quantity = command.split(': ')

    if product not in products:
        products[product] = 0
    products[product] += int(quantity)


print("Products in stock:")
[print(f"- {prod}: {quantity}") for prod, quantity in products.items()]
print(f"Total Products: {len(products)}\nTotal Quantity: {sum(products.values())}")

