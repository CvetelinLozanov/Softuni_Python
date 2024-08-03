from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    INIT_STRENGTH = 150

    def __init__(self, name: str):
        super().__init__(name, self.INIT_STRENGTH)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak: BasePeak):
        multiplier = 1.3 if peak.difficulty_level == 'Advanced' else 2.5
        self.strength -= 30 * multiplier
        self.conquered_peaks.append(peak.name)
