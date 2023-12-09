from collections import deque

chocolate = deque(int(x) for x in input().split(', '))
cups_of_milk = deque(int(x) for x in input().split(', '))
milkshake_counter = 0

while chocolate and cups_of_milk and milkshake_counter < 5:

    if cups_of_milk[0] <= 0 or chocolate[-1] <= 0:
        if cups_of_milk[0] <= 0:
            cups_of_milk.popleft()

        if chocolate[-1] <= 0:
            chocolate.pop()

    elif chocolate[-1] == cups_of_milk[0]:
        milkshake_counter += 1
        cups_of_milk.popleft()
        chocolate.pop()
    else:
        cups_of_milk.rotate(-1)
        chocolate[-1] -= 5


if milkshake_counter == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

print(f"Chocolate: {', '.join([str(x) for x in chocolate]) if chocolate else 'empty'}")
print(f"Chocolate: {', '.join([str(x) for x in cups_of_milk]) if cups_of_milk else 'empty'}")

# if chocolate:
#     chocolate_left = ', '.join([str(x) for x in chocolate])
#     print(f'Chocolate: {chocolate_left}')
# else:
#     print('Chocolate: empty')
# if cups_of_milk:
#     cups_of_milk_left = ', '.join([str(x) for x in cups_of_milk])
#     print(f'Milk: {cups_of_milk_left}')
# else:
#     print('Milk: empty')