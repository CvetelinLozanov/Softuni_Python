price_for_flour = float(input())
flour = float(input())
sugar = float(input())
eggs = int(input())
yeast = int(input())

price_for_sugar = (price_for_flour * 0.75) * sugar
eggs_price = price_for_flour * 1.10 * eggs
yeast_price = (price_for_flour * 0.75) * 0.20 * yeast
total_price_for_flour = price_for_flour * flour

total_price_for_pay = price_for_sugar + eggs_price + yeast_price + total_price_for_flour

print(f'{total_price_for_pay:.2f}')