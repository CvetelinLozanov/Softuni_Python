from project.beverage.beverage import Beverage
from project.food.cake import Cake
from project.food.food import Food
from project.food.soup import Soup
from project.product import Product

product = Product("bread", 10)
print(product.__class__.__name__)
print(product.name)
print(product.price)
food = Food("bread", 10, 10)
print(food.__class__.__name__)
print(food.__class__.__bases__[0].__name__)
print(food.name)
print(food.price)
print(food.grams)
cake = Cake("brownie")
print(cake.__class__.__name__)
print(cake.__class__.__bases__[0].__name__)
print(cake.name)
print(cake.price)
print(cake.grams)