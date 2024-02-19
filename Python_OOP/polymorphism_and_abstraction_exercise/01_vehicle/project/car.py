from project.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: float):
        needed_fuel = distance * (self.fuel_consumption + 0.9)
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel
