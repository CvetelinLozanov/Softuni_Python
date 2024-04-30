def shopping_list(budget: int, **kwargs):
    if budget < 100:
        return 'You do not have enough budget.'

    good_counter = 0
    result = []

    for k, v in kwargs.items():
        product_price, product_quantity = v
        total_expenses = product_price * product_quantity

        if budget >= total_expenses:
            result.append(f'You bought {k} for {total_expenses:.2f} leva.')
            budget -= total_expenses
            good_counter += 1

        if good_counter >= 5:
            break

    return '\n'.join(result)



print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(420, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))