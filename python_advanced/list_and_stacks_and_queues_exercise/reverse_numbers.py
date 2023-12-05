from collections import deque

numbers = deque(input().split())

while len(numbers) != 0:
    print(numbers.pop(), end=' ')
