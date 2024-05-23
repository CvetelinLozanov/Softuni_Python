from project.clients.base_client import BaseClient
from math import floor


class VIPClient(BaseClient):

    def __init__(self, name: str):
        super().__init__(name, 'VIP')

    def earning_points(self, order_amount: float):
        order_points = int(order_amount / 5)
        self.points += order_points
        return order_points

