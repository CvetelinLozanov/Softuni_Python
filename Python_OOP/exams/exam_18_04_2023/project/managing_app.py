from typing import List

from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar
from project.user import User
from project.route import Route


class ManagingApp:
    VEHICLES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = self._get_user(driving_license_number)
        if user:
            return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VEHICLES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        vehicle = self._get_vehicle(license_plate_number)
        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(self.VEHICLES[vehicle_type](brand, model, license_plate_number))
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_id = len(self.routes) + 1

        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            if route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            if route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True

        self.routes.append(Route(start_point, end_point, length, route_id))
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = self._get_user(driving_license_number)
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        vehicle = self._get_vehicle(license_plate_number)
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        route = self._get_route(route_id)
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        vehicle_status = 'OK' if not vehicle.is_damaged else 'Damaged'
        return (f"{vehicle.brand} {vehicle.model}"
                f" License plate: {license_plate_number} Battery: {vehicle.battery_level}% Status: {vehicle_status}")

    def repair_vehicles(self, count: int):
        vehicles_to_repair = self._get_damaged_vehicles()
        count_of_repaired_vehicles = min(count, len(vehicles_to_repair))

        for index in range(count_of_repaired_vehicles):
            vehicles_to_repair[index].is_damaged = False
            vehicles_to_repair[index].battery = 100

        return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = self._sort_users_by_raiting_in_descending()
        result = "*** E-Drive-Rent ***\n"
        for user in sorted_users:
            result += str(user) + '\n'

        return result.strip()

    def _get_user(self, driving_license_number: str):
        user = [user for user in self.users if driving_license_number == user.driving_license_number]
        return user[0] if user else None

    def _get_vehicle(self, license_plate_number: str):
        vehicle = [vehicle for vehicle in self.vehicles if vehicle.license_plate_number == license_plate_number]
        return vehicle[0] if vehicle else None

    def _get_route(self, route_id):
        route = [route for route in self.routes if route.route_id == route_id]
        return route[0] if route else None

    def _get_damaged_vehicles(self):
        return sorted([vehicle for vehicle in self.vehicles if vehicle.is_damaged], key=lambda x: (x.brand, x.model))

    def _sort_users_by_raiting_in_descending(self):
        return sorted(self.users, key=lambda x: -x.rating)