import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_for_meter = float(input())

total_time_for_swim = distance_in_meters * time_for_meter
slowness = (math.floor(distance_in_meters / 15)) * 12.5
total_time_for_swim += slowness

if total_time_for_swim < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {total_time_for_swim:.2f} seconds.')
else:
    print(f'No, he failed! He was {math.fabs(record_in_seconds - total_time_for_swim):.2f} seconds slower.')
