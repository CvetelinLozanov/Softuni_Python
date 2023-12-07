from collections import deque

cups = deque([int(cup)for cup in input().split()])
bottles = deque([int(bottle)for bottle in input().split()])
wasted_water = 0

while cups and bottles:

    if bottles[-1] <= cups[0]:
        cups[0] -= bottles[-1]
        bottles.pop()

        if cups[0] == 0:
            cups.popleft()

    else:
        wasted_water += abs(cups[0] - bottles[-1])
        cups.popleft()
        bottles.pop()


if cups:
    print('Cups: ', end='')
    while cups:
        print(cups.popleft(), end='')
        if cups:
            print(' ', end='')

else:
    print('Bottles: ', end='')
    while bottles:
        print(bottles.pop(), end='')
        if bottles:
            print(' ', end='')

print(f'\nWasted litters of water: {wasted_water}')