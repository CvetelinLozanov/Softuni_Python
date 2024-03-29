from typing import List
from project.dvd import DVD
from project.customer import Customer


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = [customer for customer in self.customers if customer_id == customer.id][0]
        dvd = [dvd for dvd in self.dvds if dvd_id == dvd.id][0]
        if customer.age < dvd.age_restriction:
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'

        for dvd in customer.rented_dvds:
            if dvd.id == dvd_id:
                return f'{customer.name} has already rented {dvd.name}'

        if dvd.is_rented:
            return 'DVD is already rented'

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id, dvd_id):
        customer = [customer for customer in self.customers if customer_id == customer.id][0]
        for dvd in customer.rented_dvds:
            if dvd.id == dvd_id:
                customer.rented_dvds.remove(dvd)
                dvd.is_rented = False
                return f'{customer.name} has successfully returned {dvd.name}'

        return f'{customer.name} does not have that DVD'

    def __repr__(self):
        result = []
        customers = [result.append(repr(customer)) for customer in self.customers]
        dvds = [result.append(repr(dvd)) for dvd in self.dvds]
        return '\n'.join(result)
