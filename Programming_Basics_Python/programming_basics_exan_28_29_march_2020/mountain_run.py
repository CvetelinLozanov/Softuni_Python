from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds = float(input())

slowness = floor(distance_in_meters / 50) * 30
total_time = distance_in_meters * time_in_seconds + slowness

if total_time < record_in_seconds:
    print(f'Yes! The new record is {total_time:.2f} seconds.')

else:
    print(f'No! He was {abs(record_in_seconds - total_time):.2f} seconds slower.')
