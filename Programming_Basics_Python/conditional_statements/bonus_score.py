number_of_points = int(input())
bonus_points = 0

if number_of_points % 2 == 0:
     bonus_points += 1
elif number_of_points % 10 == 5:
     bonus_points += 2

if number_of_points < 100:
     bonus_points += 5
     number_of_points += bonus_points
elif 100 < number_of_points < 1000:
    bonus_points += number_of_points * 0.2
    number_of_points += bonus_points
else:
     bonus_points += number_of_points * 0.1
     number_of_points += bonus_points

print(bonus_points)
print(number_of_points)