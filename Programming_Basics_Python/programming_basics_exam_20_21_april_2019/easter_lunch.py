easter_bread = int(input())
eggs = int(input())
cookies = int(input())

easter_bread_total_price = easter_bread * 3.20
eggs_total_price = eggs * 4.35
cookies_total_price = cookies * 5.40
paint_price = eggs * 12 * 0.15

total_price_to_pay = easter_bread_total_price + eggs_total_price + cookies_total_price + paint_price

print(f'{total_price_to_pay:.2f}')