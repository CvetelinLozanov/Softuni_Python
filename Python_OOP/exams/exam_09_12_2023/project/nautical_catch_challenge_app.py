from project.fish.base_fish import BaseFish
from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from typing import List


class NauticalCatchChallengeApp:
    DIVERS = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    FISHES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fishes: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):

        if diver_type not in self.DIVERS:
            return f"{diver_type} is not allowed in our competition."

        diver = self._get_diver(diver_name)

        if diver:
            return f"{diver_name} is already a participant."

        self.divers.append(self.DIVERS[diver_type](diver_name))
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):

        if fish_type not in self.FISHES:
            return f"{fish_type} is forbidden for chasing in our competition."

        fish = self._get_fish(fish_name)

        if fish:
            return f"{fish_name} is already permitted."

        self.fishes.append(self.FISHES[fish_type](fish_name, points))
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self._get_diver(diver_name)
        fish = self._get_fish(fish_name)

        if not diver:
            return f"{diver_name} is not registered for the competition."

        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        divers = self._get_divers_with_health_issues()
        for diver in divers:
            diver.update_health_status()
            diver.renew_oxy()

        return f"Divers recovered: {len(divers)}"

    def diver_catch_report(self, diver_name: str):
        result = f'**{diver_name} Catch Report**\n'
        diver = self._get_diver(diver_name)
        for fish in diver.catch:
            result += fish.fish_details() + "\n"

        return result.strip()

    def competition_statistics(self):
        result = '**Nautical Catch Challenge Statistics**\n'
        divers = self._get_divers_without_health_issues()
        sorted_divers = sorted(divers, key=lambda x: (-x.competition_points, -len(x.catch), x.name))
        for diver in sorted_divers:
            result += str(diver) + "\n"

        return result.strip()

    def _get_diver(self, diver_name: str):
        diver = [diver for diver in self.divers if diver_name == diver.name]
        return diver[0] if diver else None

    def _get_fish(self, fish_name: str):
        fish = [fish for fish in self.fishes if fish_name == fish.name]
        return fish[0] if fish else None

    def _get_divers_with_health_issues(self):
        return [diver for diver in self.divers if diver.has_health_issue]

    def _get_divers_without_health_issues(self):
        return [diver for diver in self.divers if not diver.has_health_issue]

