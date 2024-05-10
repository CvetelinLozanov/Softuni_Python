from collections import deque


seats = input().split(', ')
first_sequence = deque([int(num) for num in input().split(', ')])
second_sequence = deque([int(num) for num in input().split(', ')])
taken_seats = []
rotations = 0

while first_sequence and second_sequence:
    if len(taken_seats) == 3 or rotations == 10:
        break

    first_num = first_sequence.popleft()
    second_num = second_sequence.pop()
    ascii_char = chr(first_num + second_num)
    rotations += 1

    first_seat = f"{first_num}{ascii_char}"
    second_seat = f"{second_num}{ascii_char}"

    if first_seat in taken_seats or second_seat in taken_seats:
        continue

    if first_seat in seats:
        taken_seats.append(first_seat)

    elif second_seat in seats:
        taken_seats.append(second_seat)

    else:
        first_sequence.append(first_num)
        second_sequence.appendleft(second_num)

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")
