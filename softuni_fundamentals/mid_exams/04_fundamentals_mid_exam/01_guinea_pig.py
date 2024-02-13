def main_logic():
    food_in_grams = float(input()) * 1000
    hay_in_grams = float(input()) * 1000
    cover_in_grams = float(input()) * 1000
    pig_s_weight = float(input()) * 1000

    for day in range(1, 31):
        food_in_grams -= 300
        if day % 2 == 0:
            hay_to_remove = food_in_grams * 0.05
            hay_in_grams -= hay_to_remove

        if day % 3 == 0:
            cover_to_remove = pig_s_weight / 3
            cover_in_grams -= cover_to_remove

        if food_in_grams <= 0 or hay_in_grams <= 0 or cover_in_grams <= 0:
            print('Merry must go to the pet store!')
            break
    else:
        print(f'Everything is fine! Puppy is happy! Food: {food_in_grams / 1000:.2f}, '
              f'Hay: {hay_in_grams / 1000:.2f},'
              f' Cover: {cover_in_grams / 1000:.2f}.')


main_logic()
