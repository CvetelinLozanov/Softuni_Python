from collections import deque

monsters_armour = deque([int(num) for num in input().split(',')])
soldier_strikes = deque([int(num) for num in input().split(',')])
killed_monsters = 0

while monsters_armour and soldier_strikes:
    if soldier_strikes[-1] >= monsters_armour[0]:
        soldier_strikes[-1] -= monsters_armour[0]
        monsters_armour.popleft()
        killed_monsters += 1
        if len(soldier_strikes) == 1:
            if soldier_strikes[0] == 0:
                soldier_strikes.pop()
            continue

        soldier_strikes[-2] += soldier_strikes[-1]
        soldier_strikes.pop()

    elif soldier_strikes[-1] < monsters_armour[0]:
        monsters_armour[0] -= soldier_strikes[-1]
        soldier_strikes.pop()
        monsters_armour.rotate(-1)

if not monsters_armour:
    print('All monsters have been killed!')
if not soldier_strikes:
    print('The soldier has been defeated.')

print(f'Total monsters killed: {killed_monsters}')
