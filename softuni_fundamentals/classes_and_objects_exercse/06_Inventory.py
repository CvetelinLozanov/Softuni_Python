from typing import List


class Inventory:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items: List[str] = []

    def add_item(self, item: str):
        if len(self.items) >= self.__capacity:
            return f'not enough room in the inventory'

        self.items.append(item)

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f'Items: {", ".join(self.items)}.\nCapacity left: {self.__capacity - len(self.items)}'


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
