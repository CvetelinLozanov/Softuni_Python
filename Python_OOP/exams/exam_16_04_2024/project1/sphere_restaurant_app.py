from typing import List

# from exams.exam_16_04_2024.project.waiters.base_waiter import BaseWaiter
# from exams.exam_16_04_2024.project.waiters.full_time_waiter import FullTimeWaiter
# from exams.exam_16_04_2024.project.waiters.half_time_waiter import HalfTimeWaiter
# from exams.exam_16_04_2024.project.clients.base_client import BaseClient
# from exams.exam_16_04_2024.project.clients.regular_client import RegularClient
# from exams.exam_16_04_2024.project.clients.vip_client import VIPClient

from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter
from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient


class SphereRestaurantApp:
    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in ["FullTimeWaiter", "HalfTimeWaiter"]:
            return f"{waiter_type} is not a recognized waiter type."

        if waiter_name in [waiter.name for waiter in self.waiters]:
            return f"{waiter_name} is already on the staff."

        if waiter_type == 'FullTimeWaiter':
            self.waiters.append(FullTimeWaiter(waiter_name, hours_worked))
        elif waiter_type == 'HalfTimeWaiter':
            self.waiters.append(HalfTimeWaiter(waiter_name, hours_worked))

        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in ["RegularClient", "VIPClient"]:
            return f"{client_type} is not a recognized client type."

        if client_name in [client.name for client in self.clients]:
            return f"{client_name} is already a client."

        if client_type == 'RegularClient':
            self.clients.append(RegularClient(client_name))
        elif client_type == 'VIPClient':
            self.clients.append(VIPClient(client_name))

        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        waiter = [waiter for waiter in self.waiters if waiter.name == waiter_name]
        if not waiter:
            return f"No waiter found with the name {waiter_name}."

        return waiter[0].report_shift()

    def process_client_order(self, client_name: str, order_amount: float):
        client = [client for client in self.clients if client_name == client.name]

        if not client:
            return f"{client_name} is not a registered client."

        earned_points = client[0].earning_points(order_amount)
        return f"{client_name} earned {earned_points} points from the order."

    def apply_discount_to_client(self, client_name: str):
        client = [client for client in self.clients if client_name == client.name]

        if not client:
            return f"{client_name} cannot get a discount because this client is not admitted!"

        percentage, remaining_points = client[0].apply_discount()

        return f"{client_name} received a {percentage}% discount. Remaining points {remaining_points}"

    def generate_report(self):
        sorted_waiters = sorted(self.waiters, key=lambda w: w.calculate_earnings(), reverse=True)

        waiter_info = "** Waiter Details **\n"
        for waiter in sorted_waiters:
            waiter_info += str(waiter) + "\n"

        total_earnings = sum([waiter.calculate_earnings() for waiter in self.waiters])
        total_client_points = sum([client.points for client in self.clients])
        total_clients_count = len(self.clients)
        return (f"$$ Monthly Report $$\nTotal Earnings: ${total_earnings:.2f}\n"
                f"Total Clients Unused Points: {total_client_points}\n"
                f"Total Clients Count: {total_clients_count}\n"
                f"** Waiter Details **\n" + waiter_info)