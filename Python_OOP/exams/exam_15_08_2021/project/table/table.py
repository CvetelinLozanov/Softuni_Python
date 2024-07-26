from abc import ABC, abstractmethod
from typing import List

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders: List[BakedFood] = []
        self.drink_orders: List[Drink] = []
        self.number_of_people: int = 0
        self.is_reserved = False

    @property
    @abstractmethod
    def _min_num(self):
        pass

    @property
    @abstractmethod
    def _max_num(self):
        pass

    @property
    def table_number(self):
        return self.__table_number

    @property
    @abstractmethod
    def _type(self):
        pass

    @table_number.setter
    def table_number(self, value):
        if not self._min_num <= value <= self._max_num:
            raise ValueError(f"{self._type} table's number must be between {self._min_num} and {self._max_num} inclusive!")
        self.__table_number = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    #check if table have enough capacity
    def reserve(self, number_of_people: int):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        total_drink_bill = sum(d.price for d in self.drink_orders)
        total_food_bill = sum(f.price for f in self.food_orders)
        total_bill = total_food_bill + total_drink_bill
        return total_bill

    def clear(self):
        self.is_reserved = False
        self.drink_orders.clear()
        self.food_orders.clear()
        self.number_of_people = 0

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\nType: {self.__class__.__name__}\nCapacity: {self.capacity}"

