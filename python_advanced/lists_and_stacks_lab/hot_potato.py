from collections import deque

players = deque(input().split())
n = int(input()) - 1

while len(players) != 1:
    players.rotate(-n)
    print(f'Removed {players.popleft()}')

print(f'Last is {players.pop()}')