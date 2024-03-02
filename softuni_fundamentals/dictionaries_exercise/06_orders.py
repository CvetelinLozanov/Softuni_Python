def print_products(products):
    for product, info in products.items():
        print(f"{product} -> {products[product]['price'] * products[product]['quantity']:.2f}")


def process_products(products, product, price, quantity):
    if product not in products:
        products[product] = {}
        products[product]['price'] = price
        products[product]['quantity'] = quantity
    else:
        products[product]['quantity'] += quantity
        if products[product]['price'] != price:
            products[product]['price'] = price

    return products


products = {}


while True:
    command = input()

    if command == 'buy':
        break

    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    products = process_products(products, product, price, quantity)

print_products(products)
