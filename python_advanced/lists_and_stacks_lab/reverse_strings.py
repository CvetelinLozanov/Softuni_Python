from collections import deque

text = deque(input())

while len(text) != 0:
    print(text.pop(), end='')