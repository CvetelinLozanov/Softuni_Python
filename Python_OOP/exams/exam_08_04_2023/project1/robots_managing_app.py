from project.robots.base_robot import BaseRobot
from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot
from project.services.base_service import BaseService
from project.services.secondary_service import SecondaryService
from project.services.main_service import MainService
from typing import List


class RobotsManagingApp:

    SERVICES = {"MainService": MainService, "SecondaryService": SecondaryService}
    ROBOTS = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.SERVICES:
            raise Exception("Invalid service type!")

        self.services.append(self.SERVICES[service_type](name))
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.ROBOTS:
            raise Exception("Invalid robot type!")

        self.robots.append(self.ROBOTS[robot_type](name, kind, price))
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        service = self._get_service(service_name)
        robot = self._get_robot(robot_name)

        if not ((service.__class__.__name__ == "SecondaryService" and robot.__class__.__name__ == "FemaleRobot") or
                (service.__class__.__name__ == "MainService" and robot.__class__.__name__ == "MaleRobot")):
            return "Unsuitable service."
        #
        # if service.__class__.__name__ != "MainService" and robot.__class__.__name__ != "MaleRobot":
        #     return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        service.robots.append(robot)
        self.robots.remove(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self._get_service(service_name)
        robot = self._get_robot_from_service(robot_name, service)
        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self._get_service(service_name)
        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self._get_service(service_name)
        total_robots_price = sum([robot.price for robot in service.robots])
        return f"The value of service {service_name} is {total_robots_price:.2f}."

    def _get_service(self, service_name: str):
        service = [service for service in self.services if service.name == service_name]
        return service[0] if service else None

    def _get_robot(self, robot_name):
        robot = [robot for robot in self.robots if robot.name == robot_name]
        return robot[0] if robot else None

    @staticmethod
    def _get_robot_from_service(robot_name: str, service: BaseService):
        robot = [robot for robot in service.robots if robot.name == robot_name]
        return robot[0] if robot else None

    def __str__(self):
        result = ""
        for service in self.services:
            result += service.details() + "\n"

        return result.strip()