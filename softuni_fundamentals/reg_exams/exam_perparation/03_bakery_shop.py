from typing import Dict, List


def process_commands(stocks: Dict[str, int], command: str, quantity: int, food: str, total_sales: List[int]):

    if command == 'Receive':
        if quantity > 0:
            if food not in stocks:
                stocks[food] = 0
            stocks[food] += quantity

    elif command == 'Sell':
        if food not in stocks:
            print(f'You do not have any {food}.')

        elif quantity > stocks[food]:
            available_quantity = stocks[food]
            total_sales.append(available_quantity)
            del stocks[food]
            print(f"There aren't enough {food}. You sold the last {available_quantity} of them.")

        else:
            stocks[food] -= quantity
            total_sales.append(quantity)
            print(f'You sold {quantity} {food}.')
            if stocks[food] == 0:
                del stocks[food]

    return stocks, total_sales


def print_stocks(stocks: Dict[str, int], total_sales: List[int]):
    for food, quantity in stocks.items():
        print(f'{food}: {quantity}')
    print(f'All sold: {sum(total_sales)} goods')


stocks = {}
total_sells = []

while True:
    text = input()

    if text == 'Complete':
        break

    command, quantity, food = text.split()
    quantity = int(quantity)
    stocks, total_sells = process_commands(stocks, command, quantity, food, total_sells)

print_stocks(stocks, total_sells)