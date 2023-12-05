number_of_guests = int(input())

guests_list = set()

for _ in range(number_of_guests):
    guest = input()
    guests_list.add(guest)

guest = input()

while guest != 'END':

    if guest in guests_list:
        guests_list.remove(guest)

    guest = input()

print(len(guests_list))
[print(guest) for guest in sorted(guests_list)]