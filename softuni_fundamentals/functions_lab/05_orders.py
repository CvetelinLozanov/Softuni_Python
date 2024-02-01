def calculate_total_price(product: str, quantity: int) -> str:
    mapper = {
        'coffee': 1.5 * quantity,
        'water': 1 * quantity,
        'coke': 1.40 * quantity,
        'snacks': 2 * quantity
    }
    result = mapper[product]
    return f'{result:.2f}'


product = input()
quantity = int(input())
print(calculate_total_price(product, quantity))