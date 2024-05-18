from collections import deque


programmers = deque([int(programmer) for programmer in input().split()])
tasks = deque([int(task) for task in input().split()])

darth_vader_ducks = 0
thor_ducks = 0
big_blue_rubber_ducks = 0
small_yellow_rubber_ducks = 0

while programmers and tasks:
    current_programmer = programmers.popleft()
    current_task = tasks.pop()
    calculation = current_task * current_programmer

    if 0 <= calculation <= 60:
        darth_vader_ducks += 1

    elif 61 <= calculation <= 120:
        thor_ducks += 1

    elif 121 <= calculation <= 180:
        big_blue_rubber_ducks += 1

    elif 181 <= calculation <= 240:
        small_yellow_rubber_ducks += 1

    else:
        current_task -= 2
        tasks.append(current_task)
        programmers.append(current_programmer)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {darth_vader_ducks}")
print(f"Thor Ducky: {thor_ducks}")
print(f"Big Blue Rubber Ducky: {big_blue_rubber_ducks}")
print(f"Small Yellow Rubber Ducky: {small_yellow_rubber_ducks}")

