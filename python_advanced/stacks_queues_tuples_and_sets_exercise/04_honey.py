from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
symbols = deque(input().split())
honey = 0

operators = {
    '+': lambda a,b: abs(a + b),
    '-': lambda a,b: abs(a - b),
    '*': lambda a,b: abs(a * b),
    '/': lambda a,b: abs(a / b),
}

while working_bees and nectar:

    if nectar[-1] >= working_bees[0]:
        operator = symbols[0]
        if operator == '/' and nectar[-1] == 0:
            nectar.pop()
            working_bees.popleft()
            symbols.popleft()
            continue
        else:
            honey += operators[operator](working_bees[0], nectar[-1])
            nectar.pop()
            working_bees.popleft()
            symbols.popleft()
    else:
        nectar.pop()

print(f"Total honey made: {honey}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")
