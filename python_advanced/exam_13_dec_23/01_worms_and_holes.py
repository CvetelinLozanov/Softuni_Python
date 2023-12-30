from collections import deque

worms_size = [int(x) for x in input().split()]
holes_size = deque(int(x) for x in input().split())
matches_counter = 0
initial_worms_count = len(worms_size)

while worms_size and holes_size:
    worm = worms_size.pop()
    hole = holes_size.popleft()
    if worm == hole:
        matches_counter += 1
    else:
        worm -= 3
        if worm > 0:
            worms_size.append(worm)

if matches_counter > 0:
    print(f'Matches: {matches_counter}')
else:
    print('There are no matches.')

if initial_worms_count == matches_counter:
    print('Every worm found a suitable hole!')
elif not initial_worms_count == matches_counter and not worms_size:
    print('Worms left: none')
elif worms_size:
    print(f'Worms left: {", ".join(str(x) for x in worms_size)}')
if holes_size:
    print(f'Holes left: {", ".join(str(x) for x in holes_size)}')
else:
    print('Holes left: none')