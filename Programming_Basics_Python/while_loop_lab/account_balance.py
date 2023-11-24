money = 0

while True:
    text = input()

    if text == 'NoMoreMoney':
        break

    deposit = float(text)
    if deposit < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {deposit:.2f}')
    money += deposit

print(f'Total: {money:.2f}')