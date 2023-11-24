group = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_climbers = 0

for _ in range(group):
    climbers_in_group = int(input())
    if climbers_in_group <= 5:
        musala += climbers_in_group
    elif 6 <= climbers_in_group <= 12:
        monblan += climbers_in_group
    elif 13 <= climbers_in_group <= 25:
        kilimanjaro += climbers_in_group
    elif 26 <= climbers_in_group <= 40:
        k2 += climbers_in_group
    else:
        everest += climbers_in_group
    total_climbers += climbers_in_group


print(f'{musala / total_climbers * 100:.2f}%')
print(f'{monblan / total_climbers * 100:.2f}%')
print(f'{kilimanjaro / total_climbers * 100:.2f}%')
print(f'{k2 / total_climbers * 100:.2f}%')
print(f'{everest / total_climbers * 100:.2f}%')