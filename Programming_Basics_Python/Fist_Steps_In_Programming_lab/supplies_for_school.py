number_of_pens = int(input())
number_of_markers = int(input())
liters_of_table_cleaner = int(input())
discount_percantage = int(input()) / 100
packet_with_pens = 5.8
packet_with_markers = 7.2
cleaner_price_per_liter = 1.2
price_for_pens = number_of_pens * packet_with_pens
price_for_markers = number_of_markers * packet_with_markers
price_for_cleaner = liters_of_table_cleaner * cleaner_price_per_liter
total_price = price_for_cleaner + price_for_pens + price_for_markers
final_price = total_price - (total_price * discount_percantage)
print(final_price)