from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    DELICACIES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    BOOTHS = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        delicacy = self._get_delicacy(name)
        if delicacy:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        self.delicacies.append(self.DELICACIES[type_delicacy](name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth = self._get_booth(booth_number)

        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(self.BOOTHS[type_booth](booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self._get_booth(booth_number)
        delicacy = self._get_delicacy(delicacy_name)

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self._get_booth(booth_number)
        bill = booth.price_for_reservation + sum([delicacy.price for delicacy in booth.delicacy_orders])
        self.income += bill
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0
        result = f"Booth {booth_number}:\nBill: {bill:.2f}lv."
        return result.strip()

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    def _get_delicacy(self, delicacy_name):
        delicacy = [delicacy for delicacy in self.delicacies if delicacy.name == delicacy_name]
        return delicacy[0] if delicacy else None

    def _get_booth(self, booth_num):
        booth = [booth for booth in self.booths if booth.booth_number == booth_num]
        return booth[0] if booth else None
