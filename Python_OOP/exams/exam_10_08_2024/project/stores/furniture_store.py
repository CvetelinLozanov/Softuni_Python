from typing import List

from project.products.base_product import BaseProduct
from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    CAPACITY = 50

    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.CAPACITY)

    @property
    def store_type(self):
        return "FurnitureStore"

    # def store_stats(self):
    #
    #     result = [f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
    #               self.get_estimated_profit(), "**Furniture for sale:"]
    #
    #     sorted_products = sorted(self.products, key=lambda p: p.model)
    #     models_count = self.calculate_model_count(sorted_products)
    #     models_total_price = self.calculate_total_price_for_model(sorted_products)
    #     for model, count in models_count.items():
    #         result.append(f"{model}: {models_count[model]}pcs,"
    #                       f" average price: {models_total_price[model] / models_count[model]:.2f}")
    #
    #     return '\n'.join(result)

    def store_stats(self):
        products_summary = {}
        for product in self.products:
            if product.model not in products_summary:
                products_summary[product.model] = {"count": 0, "total_price": 0.0}
            products_summary[product.model]["count"] += 1
            products_summary[product.model]["total_price"] += product.price

        stats = [
            f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
            self.get_estimated_profit(),
            "**Furniture for sale:"
        ]
        for model in sorted(products_summary.keys()):
            count = products_summary[model]["count"]
            avg_price = products_summary[model]["total_price"] / count
            stats.append(f"{model}: {count}pcs, average price: {avg_price:.2f}")

        return "\n".join(stats).strip()



