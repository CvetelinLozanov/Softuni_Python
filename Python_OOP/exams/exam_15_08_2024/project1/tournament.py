from typing import List
import re
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam
from project.equipment.base_equipment import BaseEquipment
from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad


class Tournament:

    EQUIPMENT = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    TEAMS = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        pattern = r"^[0-9A-Za-z]+$"
        matches = re.findall(pattern, value)
        if not matches:
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.EQUIPMENT:
            raise Exception("Invalid equipment type!")

        equipment = self.EQUIPMENT[equipment_type]()
        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.TEAMS:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        self.teams.append(self.TEAMS[team_type](team_name, country, advantage))
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment_index = self._get_equipment_index(equipment_type)
        equipment = self.equipment[equipment_index]
        team = self._get_team(team_name)

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        team.equipment.append(equipment)
        team.budget -= equipment.price
        self.equipment.pop(equipment_index)
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self._get_team(team_name)
        if not team:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        counter = 0
        for equipment in self.equipment:
            if equipment.__class__.__name__ == equipment_type:
                counter += 1
                equipment.increase_price()

        return f"Successfully changed {counter}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_1 = self._get_team(team_name1)
        team_2 = self._get_team(team_name2)

        if team_1.__class__.__name__ != team_2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team_1_protection_points = sum([equipment.protection for equipment in team_1.equipment])
        team_2_protection_points = sum([equipment.protection for equipment in team_2.equipment])
        team_1_total_points = team_1_protection_points + team_1.advantage
        team_2_total_points = team_2_protection_points + team_2.advantage

        if team_1_total_points == team_2_total_points:
            return "No winner in this game."

        if team_1_total_points > team_2_total_points:
            team_1.win()
            return f"The winner is {team_1.name}."
        else:
            team_2.win()
            return f"The winner is {team_2.name}."

    def get_statistics(self):
        result = f"Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:\n"

        for team in sorted(self.teams, key=lambda x: -x.wins):
            result += team.get_statistics()

        return result.strip()

    def _get_team(self, team_name: str):
        team = [team for team in self.teams if team.name == team_name]
        return team[0] if team else None

    def _get_equipment_index(self, equipment_type):
        for index in range(len(self.equipment) - 1, -1, -1):
            if self.equipment[index].__class__.__name__ == equipment_type:
                return index
