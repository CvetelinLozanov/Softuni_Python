from abc import ABC, abstractmethod


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    @abstractmethod
    def _valid_processors(self):
        pass

    @property
    @abstractmethod
    def _valid_ram(self):
        pass

    @property
    @abstractmethod
    def _type(self):
        pass

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value is None:
            raise ValueError("Manufacturer name cannot be empty.")
        text_as_spaces = ' ' * len(value)
        if text_as_spaces == value:
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value is None:
            raise ValueError("Model name cannot be empty.")
        text_as_spaces = ' ' * len(value)
        if text_as_spaces == value:
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    def configure_computer(self, processor: str, ram: int):
        if processor not in self._valid_processors:
            raise ValueError(f"{processor} is not compatible with {self._type} {self.manufacturer} {self.model}!")

        if ram not in self._valid_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self._type} {self.manufacturer} {self.model}!")

        ram_price = self._valid_ram[ram] * 100
        total_price = ram_price + self._valid_processors[processor]
        self.ram = ram
        self.processor = processor
        self.price = total_price

        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

