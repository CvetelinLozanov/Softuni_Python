time_first = int(input())
time_second = int(input())
time_third = int(input())
sum_total_seconds = time_first + time_second + time_third
total_minutes = sum_total_seconds // 60
total_seconds = sum_total_seconds % 60
if total_seconds < 10:
    print(f"{total_minutes}:0{total_seconds}")
else:
    print(f"{total_minutes}:{total_seconds}")