from collections import deque

name = input()
supermarket_queue = deque()

while name != 'End':

    if name == 'Paid':
        while len(supermarket_queue) != 0:
            print(supermarket_queue.popleft())

    else:
        supermarket_queue.append(name)

    name = input()

print(f'{len(supermarket_queue)} people remaining.')