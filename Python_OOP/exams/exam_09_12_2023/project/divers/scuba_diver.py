from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):

    OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super().__init__(name, self.OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        oxygen_level = int(time_to_catch * 0.3)
        if self.oxygen_level - oxygen_level <= 0:
            self.oxygen_level = 0
            self.has_health_issue = True
        else:
            self.oxygen_level -= oxygen_level

    def renew_oxy(self):
        self.oxygen_level = self.OXYGEN_LEVEL
