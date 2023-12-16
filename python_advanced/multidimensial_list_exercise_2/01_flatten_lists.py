numbers = [x for el in input().split('|') for x in reversed(el.strip().split())]
print(*numbers[::-1])