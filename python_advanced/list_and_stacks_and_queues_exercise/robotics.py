from collections import deque

robots_list = list(input().split(";"))
free_robots_dict = {}
working_robots_dict = {}

product_deque = deque()
working_deque = deque()

for robs in robots_list:
    robot_data = robs.split("-")
    working_robots_dict[robot_data[0]] = int(robot_data[1])
    free_robots_dict[robot_data[0]] = -1

starting_time = input().split(":")
hours = int(starting_time[0])
minutes = int(starting_time[1])
seconds = int(starting_time[2])

while True:
    product = input()
    if product == "End":
        break
    product_deque.append(product)

while product_deque or working_deque:
    seconds += 1
    if product_deque:
        working_deque.append(product_deque.popleft())
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
    if hours == 24:
        hours = 0

    for rob in free_robots_dict:
        if working_deque:
            if free_robots_dict[rob] == -1:
                free_robots_dict[rob] = 0
                print(f"{rob} - {working_deque.popleft()} [{hours:02d}:{minutes:02d}:{seconds:02d}]")
                continue
            elif free_robots_dict[rob] > -1:
                free_robots_dict[rob] += 1
                if free_robots_dict[rob] >= working_robots_dict[rob]:
                    free_robots_dict[rob] = -1
                    if working_deque:
                        free_robots_dict[rob] = 0
                        print(f"{rob} - {working_deque.popleft()} [{hours:02d}:{minutes:02d}:{seconds:02d}]")
                        continue
        else:
            if free_robots_dict[rob] > -1:
                free_robots_dict[rob] += 1
                if free_robots_dict[rob] >= working_robots_dict[rob]:
                    free_robots_dict[rob] = -1
    else:
        if working_deque:
            product_deque.append(working_deque.popleft())