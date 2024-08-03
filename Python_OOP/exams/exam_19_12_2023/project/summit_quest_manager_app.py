from project.peaks.base_peak import BasePeak
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak
from project.climbers.summit_climber import SummitClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.arctic_climber import ArcticClimber
from typing import List


class SummitQuestManagerApp:

    VALID_CLIMBERS = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    VALID_PEAKS = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBERS:
            return f"{climber_type} doesn't exist in our register."

        climber = self.__find_climber_by_name(climber_name)
        if climber:
            return f"{climber_name} has been already registered."

        self.climbers.append(self.VALID_CLIMBERS[climber_type](climber_name))
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAKS:
            return f"{peak_type} is an unknown type of peak."

        self.peaks.append(self.VALID_PEAKS[peak_type](peak_name, peak_elevation))
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        climber = self.__find_climber_by_name(climber_name)
        peak = self.__find_peak_by_name(peak_name)
        gear = set(gear)
        match_set = set(peak.get_recommended_gear()) - gear

        if not match_set:
            climber.is_prepared = True
            return f"{climber_name} is prepared to climb {peak_name}."

        climber.is_prepared = False
        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(match_set))}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = self.__find_climber_by_name(climber_name)
        if not climber:
            return f"Climber {climber_name} is not registered yet."

        peak = self.__find_peak_by_name(peak_name)

        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        if not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        valid_climbers = self.__get_climbers_with_conquered_peaks()
        sorted_climbers = sorted(valid_climbers, key=lambda x: (-len(x.conquered_peaks), x.name))
        result = [f"Total climbed peaks: {sum(set([len(climber.conquered_peaks) for climber in valid_climbers]))}"
                  f"\n**Climber's statistics:**"]
        [result.append(str(climber)) for climber in sorted_climbers]

        return '\n'.join(result)

    def __find_climber_by_name(self, climber_name: str):
        return next((c for c in self.climbers if c.name == climber_name), None)

    def __find_peak_by_name(self, peak_name):
        return next((p for p in self.peaks if p.name == peak_name), None)

    def __get_climbers_with_conquered_peaks(self):
        return [c for c in self.climbers if c.conquered_peaks]