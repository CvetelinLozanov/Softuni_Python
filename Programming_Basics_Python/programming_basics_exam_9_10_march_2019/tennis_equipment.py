from math import floor, ceil

price_for_tennis_racket = float(input())
number_of_tennis_rackets = int(input())
number_of_shoes = int(input())

total_price_for_rackets = price_for_tennis_racket * number_of_tennis_rackets
total_price_for_shoes = number_of_shoes * (price_for_tennis_racket / 6)

total_price_to_pay = (total_price_for_rackets + total_price_for_shoes) * 1.20

print(f'Price to be paid by Djokovic {floor(total_price_to_pay / 8)}')
print(f'Price to be paid by sponsors {ceil(total_price_to_pay * 7 / 8)}')