from typing import Dict


class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name: str, mana_cost: float):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        result = []
        result.append(f"Name: {self.name}")
        result.append(f"Guild: {self.guild}")
        result.append(f"HP: {self.hp}")
        result.append(f"MP: {self.mp}")
        [result.append(f"==={skill} - {mana}") for skill, mana in self.skills.items()]
        return '\n'.join(result)


