from typing import List


# Function to read the prices from user and return if user is special
def reading_prices(_parts_prices: List[float], taxes: List[float]):
    is_client_special = False
    while True:
        command = input()
        if command == 'special':
            is_client_special = True
            break

        if command == 'regular':
            break

        part_price = float(command)

        if part_price < 0:
            print('Invalid price!')
            continue

        taxes.append(part_price * 0.2)
        parts_prices.append(part_price)

    return is_client_special


def print_result(total_price: float, taxes_sum: float, parts_sum):
    if total_price == 0:
        print('Invalid order!')
    else:
        print(f"Congratulations you've just bought a new computer!\n"
              f"Price without taxes: {parts_sum:.2f}$\n"
              f"Taxes: {taxes_sum:.2f}$\n"
              f"-----------\n"
              f"Total price: {total_price:.2f}$")


parts_prices = []
taxes = []
is_client_special = reading_prices(parts_prices, taxes)
taxes_sum = sum(taxes)
parts_sum = sum(parts_prices)
total_price = taxes_sum + parts_sum
if is_client_special:
    total_price *= 0.90

print_result(total_price, taxes_sum, parts_sum)


