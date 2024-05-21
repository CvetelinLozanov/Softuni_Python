from project.clients.base_client import BaseClient
from math import floor


class VIPClient(BaseClient):

    def __init__(self, name: str):
        super().__init__(name, 'VIP')

    @property
    def dollars(self):
        return 5

    # def earning_points(self, order_amount: float):
    #     amount = floor(order_amount)
    #     order_points = 0
    #     while amount >= 5:
    #         self.points += 1
    #         order_points += 1
    #         amount -= 5
    #
    #     return order_points

