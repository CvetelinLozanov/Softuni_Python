from project.animals.birds import Hen, Owl
from project.animals.mammals import Mouse
from project.food import Vegetable, Fruit, Meat

mouse = Mouse("Pip", 10, 'Azis')
print(mouse)
meat = Meat(4)
print(mouse.make_sound())
mouse.feed(meat)
veg = Vegetable(1)
print(mouse.feed(veg))
print(mouse)