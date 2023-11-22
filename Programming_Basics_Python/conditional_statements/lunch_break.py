from math import ceil

name_of_serial = input()
episode_time = int(input())
time_for_rest = int(input())

time_for_rest -= (time_for_rest / 8) + (time_for_rest / 4)

if episode_time <= time_for_rest:
    print(f"You have enough time to watch {name_of_serial} and left with {ceil(time_for_rest - episode_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_serial}, you need {ceil(episode_time - time_for_rest)} more minutes.")



