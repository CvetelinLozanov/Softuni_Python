from typing import List

from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    __valid_computers = ["Desktop Computer", "Laptop"]

    def __init__(self):
        self.warehouse:List[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.__valid_computers:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        computer = None

        if type_computer == 'Laptop':
            computer = Laptop(manufacturer, model)
        elif type_computer == 'Desktop Computer':
            computer = DesktopComputer(manufacturer, model)

        message = computer.configure_computer(processor, ram)

        self.warehouse.append(computer)
        return message

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.price <= client_budget and computer.processor == wanted_processor and computer.ram >= wanted_ram:
                profit = client_budget - computer.price
                self.profits += profit
                self.warehouse.remove(computer)
                return f"{repr(computer)} sold for {client_budget}$."
            else:
                raise Exception("Sorry, we don't have a computer for you.")

