number_of_days = int(input())
food = float(input())

biscuits = 0
total_dog_feed = 0
total_cat_feed = 0
total_feed = 0
daily_feed = 0

for day in range(1, number_of_days + 1):
    dog_feed = int(input())
    cat_feed = int(input())

    if food < total_feed:
        total_feed = food
        total_dog_feed = food
        total_cat_feed = food
        break

    total_dog_feed += dog_feed
    total_cat_feed += cat_feed
    total_feed += dog_feed + cat_feed
    daily_feed = dog_feed + cat_feed

    if day % 3 == 0:

        biscuits += daily_feed * 0.10

print(f'Total eaten biscuits: {round(biscuits)}gr.')
print(f'{total_feed / food * 100:.2f}% of the food has been eaten.')
print(f'{total_dog_feed / total_feed * 100:.2f}% eaten from the dog.')
print(f'{total_cat_feed / total_feed * 100:.2f}% eaten from the cat.')
