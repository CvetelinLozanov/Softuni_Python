from typing import List
from project.astronaut.astronaut import Astronaut
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository
from project.astronaut.astronaut_repository import AstronautRepository


class SpaceStation:

    VALID_ASTRONAUTS = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist
    }
    number_of_successful_missions = 0
    number_of_unsuccessful_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.VALID_ASTRONAUTS:
            raise Exception("Astronaut type is not valid!")

        astronaut = self.planet_repository.find_by_name(name)
        if astronaut:
            return f"{name} is already added."

        self.astronaut_repository.add(self.VALID_ASTRONAUTS[astronaut_type](name))
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        planet = self.planet_repository.find_by_name(name)
        if planet:
            return f"{name} is already added."

        items = items.split(', ')
        planet = Planet(name)
        planet.items.extend(items)
        # test with extend
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)

        if not planet:
            raise Exception("Invalid planet name!")

        suitable_astronauts = sorted([a for a in self.astronaut_repository.astronauts if a.oxygen > 30],
                                     key=lambda a: -a.oxygen)[:5]

        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts_in_open_space = 0
        for a in suitable_astronauts:
            astronauts_in_open_space += 1
            for i in range(len(planet.items)):
                if a.oxygen < 1:
                    break
                item = planet.items.pop()
                a.backpack.append(item)
                a.breathe()

        if not planet.items:
            self.number_of_successful_missions += 1
            return (f"Planet: {planet.name} was explored. {astronauts_in_open_space}"
                    f" astronauts participated in collecting items.")
        self.number_of_unsuccessful_missions += 1
        return "Mission is not completed."

    def report(self):
        result = [f"{self.number_of_successful_missions} successful missions!\n"
                  f"{self.number_of_unsuccessful_missions} missions were not completed!\n"
                  f"Astronauts' info:"]
        for a in self.astronaut_repository.astronauts:
            result.append(f"Name: {a.name}")
            result.append(f"Oxygen: {a.oxygen}")
            result.append(f"Backpack items: {', '.join(a.backpack) if a.backpack else 'none'}")

        return '\n'.join(result)


# babylon5 = SpaceStation()
# print(babylon5.add_astronaut("Biologist", "Plant"))
# print(babylon5.add_astronaut("Geodesist", "Geo"))
# print(babylon5.add_astronaut("Meteorologist", "Meteo"))
# for a in [a for a in babylon5.astronaut_repository.astronauts]:
#     print(a.name)
#     print(a.oxygen)
#     a.breathe()
#     print(a.oxygen)
#     a.increase_oxygen(7)
#     print(a.oxygen)
#     print(str(a.initial_oxygen))
# print(babylon5.add_planet("Mars", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23"))
#
# for p in [p for p in babylon5.planet_repository.planets]:
#     print(p.name)
#     print(p.items)
#
# print(babylon5.add_planet("Mars", "Hammer, Xbox, Socks"))
# print(babylon5.retire_astronaut("Meteo"))
# # print(babylon5.retire_astronaut("Maon4o"))
# babylon5.recharge_oxygen()
# # print(babylon5.add_astronaut("Meteorologist", "Meteo Jr."))
# for a in [a for a in babylon5.astronaut_repository.astronauts]:
#     print(a.name)
#     print(a.oxygen)
#     print(str(a.initial_oxygen))
#
# # print(babylon5.add_astronaut("Biologist", "Plant2"))
# # print(babylon5.add_astronaut("Biologist", "Plant3"))
# # print(babylon5.add_astronaut("Geodesist", "Geo2"))
# # print(babylon5.add_astronaut("Geodesist", "Geo3"))
# # print(babylon5.add_astronaut("Meteorologist", "Meteo Sr"))
# # print(babylon5.add_astronaut("Meteorologist", "Meteo Sr2"))
# print(babylon5.send_on_mission("Mars"))
# print(babylon5.report())