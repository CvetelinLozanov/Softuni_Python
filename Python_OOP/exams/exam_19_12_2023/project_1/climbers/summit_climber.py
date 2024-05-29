from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):

    INITIAL_STRENGTH = 150

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak: BasePeak):
        peak_difficulty = peak.calculate_difficulty_level()
        self.strength -= 30 * 1.3 if peak_difficulty == 'Advanced' else 30 * 2.5
        self.conquered_peaks.append(peak.name)
