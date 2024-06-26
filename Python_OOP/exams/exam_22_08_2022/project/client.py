import re
from typing import List
from project.meals.meal import Meal


class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: List[Meal] = []
        self.bill = 0.0
        self.ordered_meals = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        pattern = r"\b[0][0-9]{9}\b"
        matches = re.findall(pattern, value)
        if not matches:
            raise ValueError("Invalid phone number!")
        self.__phone_number = value
