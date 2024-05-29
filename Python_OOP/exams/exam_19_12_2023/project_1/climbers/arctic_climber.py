from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):

    INITIAL_STRENGTH = 200

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= 100

    def climb(self, peak: BasePeak):
        peak_difficulty = peak.calculate_difficulty_level()
        self.strength -= 20 * 2 if peak_difficulty == 'Extreme' else 20 * 1.5
        self.conquered_peaks.append(peak.name)
