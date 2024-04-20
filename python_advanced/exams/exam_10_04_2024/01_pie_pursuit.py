from collections import deque


contestants = deque([int(con) for con in input().split()])
pies = deque([int(pie) for pie in input().split()])

while pies and contestants:
    current_pie = pies[-1]
    current_contestant = contestants[0]

    if current_contestant >= current_pie:
        pies.pop()
        contestants.popleft()
        current_contestant -= current_pie
        if current_contestant > 0:
            contestants.append(current_contestant)

    else:
        current_pie -= current_contestant
        contestants.popleft()
        pies.pop()

        if pies and current_pie == 1:
            pies[-1] += current_pie
        else:
            pies.append(current_pie)


if not pies and contestants:
    print('We will have to wait for more pies to be baked!')
    print(f'Contestants left: {", ".join(map(str, contestants))}')
elif not pies and not contestants:
    print('We have a champion!')
else:
    print('Our contestants need to rest!')
    print(f'Pies left: {", ".join(map(str, pies))}')


