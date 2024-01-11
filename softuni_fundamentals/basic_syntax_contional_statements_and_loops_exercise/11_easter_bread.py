budget = float(input())

price_for_kg_flour = float(input())
pack_of_eggs = price_for_kg_flour * 0.75
liter_milk_price = price_for_kg_flour * 1.25
total_price_for_loaf = price_for_kg_flour + pack_of_eggs + (liter_milk_price / 4)

eggs_count = 0
loaves_count = 0

while budget > total_price_for_loaf:
    loaves_count += 1
    eggs_count += 3

    if loaves_count % 3 == 0:
        eggs_count -= loaves_count - 2

    budget -= total_price_for_loaf

print(f'You made {loaves_count} loaves of Easter bread! Now you have {eggs_count} eggs and {budget:.2f}BGN left.')
