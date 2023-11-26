control_minutes = int(input())
control_seconds = int(input())

length_in_meters = float(input())
seconds_for_100_meters = int(input())

control_minutes_to_seconds = control_minutes * 60
control_seconds += control_minutes_to_seconds

slowness = (length_in_meters / 120) * 2.5

marin_time = (length_in_meters / 100) * seconds_for_100_meters - slowness

if marin_time <= control_seconds:
    print(f'Marin Bangiev won an Olympic quota!\nHis time is {marin_time:.3f}.')

else:
    print(f'No, Marin failed! He was {marin_time - control_seconds:.3f} second slower.')
