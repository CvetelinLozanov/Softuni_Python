from typing import List
from project.car.car import Car
from project.driver import Driver
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.race import Race


class Controller:
    CARS = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    #problematic
    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = self.__find_car_by_model(model)

        if car:
            raise Exception(f"Car {model} is already created!")

        if car_type in self.CARS:
            self.cars.append(self.CARS[car_type](model, speed_limit))
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = self.__find_driver_by_name(driver_name)

        if driver:
            raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = self.__find_race_by_name(race_name)
        if race:
            raise Exception(f"Race {race_name} is already created!")

        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver_by_name(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        car = self.__find_last_car_from_type(car_type)

        if not car:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car:
            old_car = driver.car
            old_car.is_taken = False
            driver.car = car
            car.is_taken = True
            return f"Driver {driver.name} changed his car from {old_car.model} to {car.model}."

        if not car.is_taken:
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race_by_name(race_name)
        driver = self.__find_driver_by_name(driver_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_race_by_name(race_name)

        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners = self.__get_winners(race)
        return self.__print_winners(winners, race)

    def __find_car_by_model(self, model: str):
        return next((car for car in self.cars if car.model == model), None)

    def __find_driver_by_name(self, driver_name):
        return next((driver for driver in self.drivers if driver.name == driver_name), None)

    def __find_race_by_name(self, race_name):
        return next((race for race in self.races if race_name == race.name), None)

    def __find_last_car_from_type(self, car_type: str):
        for i in range(len(self.cars) - 1, -1, -1):
            if self.cars[i].__class__.__name__ == car_type and not self.cars[i].is_taken:
                return self.cars[i]

    @staticmethod
    def __print_winners(winners, race):
        result = []
        for i in range(len(winners)):
            result.append(f"Driver {winners[i].name} wins the {race.name} "
                          f"race with a speed of {winners[i].car.speed_limit}.")
        return '\n'.join(result)

    @staticmethod
    def __get_winners(race: Race):
        race.drivers.sort(key=lambda x: -x.car.speed_limit)
        count = 3 if len(race.drivers) >= 3 else len(race.drivers)
        for i in range(count):
            race.drivers[i].number_of_wins += 1

        return race.drivers[:3]
