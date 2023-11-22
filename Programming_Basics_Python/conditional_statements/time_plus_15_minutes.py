hours = int(input())
minutes = int(input())
total_minutes = minutes + 15
if total_minutes >= 60:
    hours += 1
    total_minutes %= 60
    if hours > 23:
        hours = 0
print(f"{hours}:{total_minutes:02d}")
