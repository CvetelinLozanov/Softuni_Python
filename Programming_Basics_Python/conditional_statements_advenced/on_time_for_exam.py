from math import  fabs

exam_hour = int(input())
exam_minutes = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())

exam_hours_in_minutes = exam_hour * 60
arrival_hours_in_minutes = arrival_hours * 60
exam_minutes += exam_hours_in_minutes
arrival_minutes += arrival_hours_in_minutes
difference = int(fabs(exam_minutes - arrival_minutes))

if difference == 0:
    print('On time')
elif exam_minutes > arrival_minutes:
    if difference <= 30:
        print(f'On time\n{difference} minutes before the start')
    elif 30 < difference < 60:
        print(f'Early\n{difference} minutes before the start')
    elif difference >= 60:
        hours = int(difference // 60)
        minutes = int(difference % 60)
        print(f'Early\n{hours}:{minutes:02d} hours before the start')
elif exam_minutes < arrival_minutes:
    if difference >= 60:
        hours = int(difference // 60)
        minutes = int(difference % 60)
        print(f'Late\n{hours}:{minutes:02d} hours after the start"')
    else:
        print(f'Late\n{difference} minutes after the start')
