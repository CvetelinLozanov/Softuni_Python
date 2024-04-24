from collections import deque


males = [int(male) for male in input().split()]
females = deque([int(female) for female in input().split()])
matches = 0

while males and females:

    if males[-1] <= 0:
        males.pop()
        continue

    if males[-1] % 25 == 0:
        males.pop()
        males.pop()
        continue

    if females[0] <= 0:
        females.popleft()
        continue

    if females[0] % 25 == 0:
        females.popleft()
        females.popleft()
        continue

    if males and females:
        current_male = males[-1]
        current_female = females[0]

        if current_female == current_male:
            females.popleft()
            males.pop()
            matches += 1

        else:
            females.popleft()
            males[-1] -= 2


print(f"Matches: {matches}")
if not males:
    print("Males left: none")
else:
    print(f"Males left: {', '.join(map(str, reversed(males)))}")

if not females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join(map(str, females))}")