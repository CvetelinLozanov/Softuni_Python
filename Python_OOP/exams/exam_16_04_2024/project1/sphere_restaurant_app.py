from typing import List

from project.clients.base_client import BaseClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.clients.vip_client import VIPClient
from project.clients.regular_client import RegularClient


class SphereRestaurantApp:

    WAITERS = {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}
    CLIENTS = {"RegularClient": RegularClient, "VIPClient": VIPClient}

    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.WAITERS:
            return f"{waiter_type} is not a recognized waiter type."

        waiter = self.__find_waiter_by_name(waiter_name)

        if waiter:
            return f"{waiter_name} is already on the staff."

        self.waiters.append(self.WAITERS[waiter_type](waiter_name, hours_worked))
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.CLIENTS:
            return f"{client_type} is not a recognized client type."

        client = self.__find_client_by_name(client_name)

        if client:
            return f"{client_name} is already a client."

        self.clients.append(self.CLIENTS[client_type](client_name))
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        waiter = self.__find_waiter_by_name(waiter_name)
        if not waiter:
            return f"No waiter found with the name {waiter_name}."

        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float):
        client = self.__find_client_by_name(client_name)

        if not client:
            return f"{client_name} is not a registered client."

        earned_points = client.earning_points(order_amount)
        return f"{client_name} earned {earned_points} points from the order."

    def apply_discount_to_client(self, client_name: str):
        client = self.__find_client_by_name(client_name)
        if not client:
            return f"{client_name} cannot get a discount because this client is not admitted!"

        discount, remaining_points = client.apply_discount()
        return f"{client_name} received a {discount}% discount. Remaining points {remaining_points}"

    def generate_report(self):
        total_earnings = sum(w.calculate_earnings() for w in self.waiters)
        total_clients_unused_points = sum(c.points for c in self.clients)
        total_clients = len(self.clients)
        sorted_waiters = sorted(self.waiters, key=lambda w: -w.calculate_earnings())
        result = (f"$$ Monthly Report $$\nTotal Earnings: ${total_earnings:.2f}\n"
                  f"Total Clients Unused Points: {total_clients_unused_points}\n"
                  f"Total Clients Count: {total_clients}\n** Waiter Details **\n")

        for waiter in sorted_waiters:
            result += str(waiter) + "\n"

        return result.strip()

    def __find_waiter_by_name(self, waiter_name: str):
        return next((w for w in self.waiters if w.name == waiter_name), None)

    def __find_client_by_name(self, client_name: str):
        return next((c for c in self.clients if c.name == client_name), None)
