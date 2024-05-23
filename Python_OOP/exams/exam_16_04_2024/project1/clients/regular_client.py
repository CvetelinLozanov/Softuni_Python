#from exams.exam_16_04_2024.project.clients.base_client import BaseClient
from project.clients.base_client import BaseClient
from math import floor


class RegularClient(BaseClient):

    def __init__(self, name: str):
        super().__init__(name, 'Regular')

    def earning_points(self, order_amount: float):
        order_points = int(order_amount / 10)
        self.points += order_points
        return order_points

