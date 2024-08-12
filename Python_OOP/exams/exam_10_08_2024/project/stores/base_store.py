from abc import ABC, abstractmethod
from typing import List

from project.products.base_product import BaseProduct


class BaseStore(ABC):
    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: List[BaseProduct] = []

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Store name cannot be empty!")
        self.__name = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if len(value.strip()) != 3:
            raise ValueError("Store location must be 3 chars long!")
        self.__location = value
        
    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity = value

    def get_estimated_profit(self):
        stock_prices = sum([p.price for p in self.products])
        profit = stock_prices * 0.10
        return f"Estimated future profit for {len(self.products)} products is {profit:.2f}"
    
    @property
    @abstractmethod
    def store_type(self):
        pass

    def store_stats(self):
        pass

    @staticmethod
    def calculate_model_count(products: List[BaseProduct]):
        models = {}
        for p in products:
            if p.model not in models:
                models[p.model] = 0
            models[p.model] += 1

        return models

    @staticmethod
    def calculate_total_price_for_model(products: List[BaseProduct]):
        models_price = {}
        for p in products:
            if p.model not in models_price:
                models_price[p.model] = 0
            models_price[p.model] += p.price

        return models_price