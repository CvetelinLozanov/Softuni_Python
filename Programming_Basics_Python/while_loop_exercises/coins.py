cashback = float(input())
cashback = int(cashback * 100)
number_of_coins = 0

while cashback > 0:
    if cashback >= 200:
        cashback -= 200
        number_of_coins += 1

    elif 100 <= cashback < 200:
        cashback -= 100
        number_of_coins += 1

    elif 50 <= cashback < 100:
        cashback -= 50
        number_of_coins += 1

    elif 20 <= cashback < 50:
        cashback -= 20
        number_of_coins += 1

    elif 10 <= cashback < 20:
        cashback -= 10
        number_of_coins += 1

    elif 5 <= cashback < 10:
        cashback -= 5
        number_of_coins += 1

    elif 2 <= cashback < 5:
        cashback -= 2
        number_of_coins += 1

    elif 1 <= cashback < 2:
        cashback -= 1
        number_of_coins += 1


print(number_of_coins)