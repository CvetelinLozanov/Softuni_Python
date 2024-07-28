from typing import List
import re
from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:

    VALID_EQUIPMENT = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAMS = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

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
        pattern = r'^[a-zA-Z0-9]+$'
        matches = re.findall(pattern, value)
        if not matches:
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT:
            raise Exception("Invalid equipment type!")

        equipment = self.VALID_EQUIPMENT[equipment_type]()
        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS:
            raise Exception("Invalid team type!")

        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."

        team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = self.__find_team_by_name(team_name)
        equipment = self.__take_last_equipment_by_type(equipment_type)
        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self.__find_team_by_name(team_name)

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
                equipment.increase_price()
                counter += 1

        return f"Successfully changed {counter}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_1 = self.__find_team_by_name(team_name1)
        team_2 = self.__find_team_by_name(team_name2)

        if team_1.__class__.__name__ != team_2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        if team_1 == team_2:
            return "No winner in this game."

        if team_1 > team_2:
            team_1.win()
            return f"The winner is {team_1.name}."
        else:
            team_2.win()
            return f"The winner is {team_2.name}."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        result = [f"Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:"]

        for team in sorted_teams:
            result.append(team.get_statistics())

        return '\n'.join(result)

    def __find_team_by_name(self, team_name: str):
        return next((t for t in self.teams if t.name == team_name), None)

    def __take_last_equipment_by_type(self, equipment_type: str):
        return [e for e in self.equipment if e.__class__.__name__ == equipment_type][-1]


