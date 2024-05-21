from abc import ABC, abstractmethod
from math import floor


class BaseClient(ABC):
    def __init__(self, name: str, membership_type: str):
        self.name = name
        self.membership_type = membership_type
        self.points = 0


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Client name should be determined!")
        self.__name = value

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value):
        if value not in ['Regular', 'VIP']:
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")
        self.__membership_type = value

    @property
    @abstractmethod
    def dollars(self):
        pass

    def earning_points(self, order_amount: float):
        amount = floor(order_amount)
        order_points = 0
        while amount >= self.dollars:
            self.points += 1
            order_points += 1
            amount -= self.dollars

        return f"{self.name} earned {order_points} points from the order."

    def apply_discount(self):
        discount_percentage = 0
        if self.points >= 100:
            discount_percentage = 10
            self.points -= 100

        elif 50 <= self.points < 100:
            discount_percentage = 5
            self.points -= 50

        return f"{self.name} received a {discount_percentage}% discount. Remaining points {self.points}"
