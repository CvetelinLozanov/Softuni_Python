items = input().split('|')
budget = float(input())
initial_budget = budget
bought_items = []

for item in items:
    item_args = item.split('->')
    item_type = item_args[0]
    item_price = float(item_args[1])

    if item_type == 'Clothes':
        if item_price <= 50:
            if budget >= item_price:
                budget -= item_price
                bought_items.append(item_price * 1.40)

    elif item_type == 'Shoes':
        if item_price <= 35:
            if budget >= item_price:
                budget -= item_price
                bought_items.append(item_price * 1.40)

    elif item_type == 'Accessories':
        if item_price <= 20.50:
            if budget >= item_price:
                budget -= item_price
                bought_items.append(item_price * 1.40)

collected_budget = sum(bought_items) + budget
profit = collected_budget - initial_budget

print(' '.join([f'{item:.2f}' for item in bought_items]))
print(f'Profit: {profit:.2f}')

if collected_budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
