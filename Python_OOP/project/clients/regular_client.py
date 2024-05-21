from project.clients.base_client import BaseClient
from math import floor


class RegularClient(BaseClient):

    def __init__(self, name: str):
        super().__init__(name, 'Regular')

    @property
    def dollars(self):
        return 10
    # def earning_points(self, order_amount: float):
    #     amount = floor(order_amount)
    #     order_points = 5
    #     while amount >= 10:
    #         self.points += 1
    #         order_points += 1
    #         amount -= 10
    #
    #     return order_points

