needed_nylon = int(input())
needed_paint = int(input())
needed_thinner = int(input())
needed_hours = int(input())
price_for_nylon_per_square_meter = 1.5
price_for_paint_per_liter = 14.50
price_for_thinner_per_liter = 5
price_for_bag = 0.4
total_price_for_nylon = (needed_nylon + 2) * price_for_nylon_per_square_meter
total_price_for_paint = (needed_paint * 1.1) * price_for_paint_per_liter
total_price_for_thinner = needed_thinner * price_for_thinner_per_liter
total_sum_for_all = price_for_bag + total_price_for_thinner + total_price_for_paint + total_price_for_nylon
pay_for_workers = (total_sum_for_all * 0.3) * needed_hours
final_price_to_pay = total_sum_for_all + pay_for_workers
print(final_price_to_pay)
