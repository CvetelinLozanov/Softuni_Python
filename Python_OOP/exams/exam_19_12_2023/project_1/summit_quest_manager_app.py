from project.peaks.summit_peak import SummitPeak
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.climbers.base_climber import BaseClimber
from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from typing import List


class SummitQuestManagerApp():
    CLIMBERS = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    PEAKS = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.CLIMBERS:
            return f"{climber_type} doesn't exist in our register."

        climber = self.get_climber(climber_name)
        if climber:
            return f"{climber_name} has been already registered."

        self.climbers.append(self.CLIMBERS[climber_type](climber_name))
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.PEAKS:
            return f"{peak_type} is an unknown type of peak."

        self.peaks.append(self.PEAKS[peak_type](peak_name, peak_elevation))
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        peak = self.get_peak(peak_name)
        climber = self.get_climber(climber_name)
        required_gear = set(peak.get_recommended_gear())
        missing_gear = required_gear - set(gear)
        if not missing_gear:
            return f"{climber_name} is prepared to climb {peak_name}."
        sorted_missing_gear = sorted(missing_gear)
        climber.is_prepared = False
        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted_missing_gear)}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        peak = self.get_peak(peak_name)
        climber = self.get_climber(climber_name)

        if not climber:
            return f"Climber {climber_name} is not registered yet."

        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        if not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

        climber.climb(peak)
        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

    def get_statistics(self):
        result = ''
        successful_climbers = [climber for climber in self.climbers if len(climber.conquered_peaks) > 0]
        sorted_climbers = sorted(successful_climbers, key=lambda x: (-len(x.conquered_peaks), x.name))
        num_of_conquered_peaks = len(set(peak for climber in self.climbers
                                    if len(climber.conquered_peaks) > 0 for peak in climber.conquered_peaks))
        result += f"Total climbed peaks: {num_of_conquered_peaks}\n"
        result += f"**Climber's statistics:**\n"
        for climber in sorted_climbers:
            result += str(climber) + "\n"

        return result.strip()

    def get_climber(self, climber_name: str):
        climber = [climber for climber in self.climbers if climber_name == climber.name]
        return climber[0] if climber else None

    def get_peak(self, peak_name: str):
        peak = [peak for peak in self.peaks if peak_name == peak.name]
        return peak[0] if peak else None