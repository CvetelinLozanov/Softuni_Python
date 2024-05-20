#from collections import deque
#
#robots_list = list(input().split(";"))
#free_robots_dict = {}
#working_robots_dict = {}
#
#product_deque = deque()
#working_deque = deque()
#
#for robs in robots_list:
#    robot_data = robs.split("-")
#    working_robots_dict[robot_data[0]] = int(robot_data[1])
#    free_robots_dict[robot_data[0]] = -1
#
#starting_time = input().split(":")
#hours = int(starting_time[0])
#minutes = int(starting_time[1])
#seconds = int(starting_time[2])
#
#while True:
#    product = input()
#    if product == "End":
#        break
#    product_deque.append(product)
#
#while product_deque or working_deque:
#    seconds += 1
#    if product_deque:
#        working_deque.append(product_deque.popleft())
#    if seconds == 60:
#        seconds = 0
#        minutes += 1
#    if minutes == 60:
#        minutes = 0
#        hours += 1
#    if hours == 24:
#        hours = 0
#
#    for rob in free_robots_dict:
#        if working_deque:
#            if free_robots_dict[rob] == -1:
#                free_robots_dict[rob] = 0
#                print(f"{rob} - {working_deque.popleft()} [{hours:02d}:{minutes:02d}:{seconds:02d}]")
#                continue
#            elif free_robots_dict[rob] > -1:
#                free_robots_dict[rob] += 1
#                if free_robots_dict[rob] >= working_robots_dict[rob]:
#                    free_robots_dict[rob] = -1
#                    if working_deque:
#                        free_robots_dict[rob] = 0
#                        print(f"{rob} - {working_deque.popleft()} [{hours:02d}:{minutes:02d}:{seconds:02d}]")
#                        continue
#        else:
#            if free_robots_dict[rob] > -1:
#                free_robots_dict[rob] += 1
#                if free_robots_dict[rob] >= working_robots_dict[rob]:
#                    free_robots_dict[rob] = -1
#    else:
#        if working_deque:
#            product_deque.append(working_deque.popleft())

from collections import deque
 
 
robots_data = input().split(';')
robots_list = []
for robot in robots_data:
    robot_name, process_time = robot.split('-')
    robots_list.append({'name': robot_name, 'process_time': int(process_time), 'busy_until_time': 0})
 
hours, minutes, seconds = [int(x) for x in input().split(':')]
start_time_seconds = hours * 3600 + minutes * 60 + seconds
 
products = deque()
while True:
    product = input()
    if product == 'End':
        break
    products.append(product)
 
while products:
    current_product = products.popleft()
    start_time_seconds += 1
    is_taken = False
    for robot in robots_list:
        if robot['busy_until_time'] <= start_time_seconds:
            robot['busy_until_time'] = start_time_seconds + robot['process_time']
            h = start_time_seconds // 3600
            m = (start_time_seconds % 3600) // 60
            s = (start_time_seconds % 3600) % 60
            h %= 24
            print(f"{robot['name']} - {current_product} [{h:02d}:{m:02d}:{s:02d}]")
            is_taken = True
            break
    if not is_taken:
        products.append(current_product)
