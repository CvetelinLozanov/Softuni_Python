food_in_kilograms = int(input())
food_in_grams = food_in_kilograms * 1000

command = input()

while command != 'Adopted':
    dog_feed_in_grams = int(command)
    food_in_grams -= dog_feed_in_grams
    command = input()

if food_in_grams >= 0:
    print(f'Food is enough! Leftovers: {food_in_grams} grams.')

else:
    print(f'Food is not enough. You need {abs(food_in_grams)} grams more.')