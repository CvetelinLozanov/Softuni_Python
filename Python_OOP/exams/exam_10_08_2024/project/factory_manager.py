from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.toy_store import ToyStore
from project.stores.furniture_store import FurnitureStore
from typing import List

class FactoryManager:

    VALID_ITEMS = {"Chair": Chair, "HobbyHorse": HobbyHorse}
    VALID_STORES = {"FurnitureStore": FurnitureStore, "ToyStore": ToyStore}

    def __init__(self, name: str):
        self.name = name
        self.income = 0.0
        self.products: List[BaseProduct] = []
        self.stores: List[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self.VALID_ITEMS:
            raise Exception("Invalid product type!")

        product = self.VALID_ITEMS[product_type](model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self.VALID_STORES:
            raise Exception(f"{store_type} is an invalid type of store!")

        self.stores.append(self.VALID_STORES[store_type](name, location))
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        purchased_products = []
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        for product in products:
            if ((store.store_type == 'FurnitureStore' and product.sub_type == 'Furniture') or
                    (store.store_type == 'ToyStore' and product.sub_type == 'Toys')):
                store.products.append(product)
                self.products.remove(product)
                purchased_products.append(product)

        if len(purchased_products) == 0:
            return "Products do not match in type. Nothing sold."

        store.capacity -= len(purchased_products)
        self.income += sum(p.price for p in store.products)
        return f"Store {store.name} successfully purchased {len(purchased_products)} items."

    def unregister_store(self, store_name: str):
        store = self.__find_store_by_name(store_name)

        if not store:
            raise Exception("No such store!")

        if store.products:
            return f"The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model: str):
        counter = 0
        for p in self.products:
            if p.model == product_model:
                p.discount()
                counter += 1

        return f"Discount applied to {counter} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = self.__find_store_by_name(store_name)
        if not store:
            return f"There is no store registered under this name!"

        return store.store_stats()

    def statistics(self):
        products_price = sum(p.price for p in self.products)
        unsold_models = BaseStore.calculate_model_count(self.products)
        result = [f"Factory: {self.name}\nIncome: {self.income:.2f}\n***Products Statistics***\n"
                  f"Unsold Products: {len(self.products)}. Total net price: {products_price:.2f}"]
        for k, v in sorted(unsold_models.items(), key=lambda kvp: kvp[0]):
            result.append(f"{k}: {v}")

        result.append(f"***Partner Stores: {len(self.stores)}***")

        for store in sorted(self.stores, key=lambda s: s.name):
            result.append(store.name)

        return '\n'.join(result)

    def __find_store_by_name(self, store_name: str):
        return next((store for store in self.stores if store.name == store_name), None)