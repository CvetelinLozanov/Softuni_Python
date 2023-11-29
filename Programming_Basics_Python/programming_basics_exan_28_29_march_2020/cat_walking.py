minutes_for_walk = int(input())
number_of_walks = int(input())
cat_calories = int(input())

total_minutes = minutes_for_walk * number_of_walks
calories_for_day = total_minutes * 5

target_calories = cat_calories / 2

if calories_for_day >= target_calories:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {calories_for_day}.')

else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {calories_for_day}.')