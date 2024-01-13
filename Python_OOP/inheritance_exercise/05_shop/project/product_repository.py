from project.product import Product
from typing import List


class ProductRepository:

    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        if product not in self.products:
            self.products.append(product)

    def find(self, product_name: str):

        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str):

        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)

    def __repr__(self):
        return '\n'.join([f'{pr.name}: {pr.quantity}' for pr in self.products])
