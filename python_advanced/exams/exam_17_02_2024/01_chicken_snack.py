from collections import deque


money = [int(num) for num in input().split()]
food_prices = deque([int(price) for price in input().split()])

food_counter = 0

while money and food_prices:
    current_money = money[-1]
    current_food_price = food_prices[0]

    if current_money == current_food_price:
        money.pop()
        food_prices.popleft()
        food_counter += 1

    elif current_money > current_food_price:
        food_counter += 1
        food_prices.popleft()
        money.pop()
        if not money:
            money.append(current_money - current_food_price)
        else:
            money[-1] += current_money - current_food_price

    elif current_food_price > current_money:
        money.pop()
        food_prices.popleft()


if food_counter >= 4:
    print(f'Gluttony of the day! Henry ate {food_counter} foods.')
elif food_counter == 0:
    print('Henry remained hungry. He will try next weekend again.')
else:
    if food_counter == 1:
        print(f'Henry ate: {food_counter} food.')
    else:
        print(f'Henry ate: {food_counter} foods.')