number_of_chicken_menu = int(input())
number_of_fish_menu = int(input())
number_of_vegetarian_menu = int(input())
price_for_chicken_menu = 10.35
price_for_fish_menu = 12.4
price_for_vegetarian_menu = 8.15
price_for_delivery = 2.5
total_price_for_chicken = number_of_chicken_menu * price_for_chicken_menu
total_price_for_fish = number_of_fish_menu * price_for_fish_menu
total_price_for_vegetarian = number_of_vegetarian_menu * price_for_vegetarian_menu
total_price_for_all_menus = total_price_for_fish + total_price_for_chicken + total_price_for_vegetarian
price_for_dessert = total_price_for_all_menus * 0.2
final_price_to_pay = price_for_dessert + total_price_for_all_menus + 2.5
print(final_price_to_pay)