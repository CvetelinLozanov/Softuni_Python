from project.bakery import Bakery

b = Bakery("test")
print(b.add_drink("Tea", "menta", 10, "some"))
print(b.add_drink("Water", "izvorna", 10, "bankq"))
print(b.add_food("Bread", "dob", 10))
print(b.add_food("Bread", "ruch", 10))
print(b.add_food("Cake", "brown", 10))
print([food.portion for food in b.food_menu])
print(b.add_table("OutsideTable", 51, 10))
print(b.add_table("InsideTable", 23, 5))
print(b.order_food(51, "dob", "ruch", "bokluk"))
print(b.order_drink(51, "menta", "izvorna", "brown"))
print(b.reserve_table(6))
print('--------')
print(b.get_free_tables_info())
print('--------')
print(b.leave_table(51))
print('--------')
print(b.get_free_tables_info())
print('--------')
print(b.get_total_income())
