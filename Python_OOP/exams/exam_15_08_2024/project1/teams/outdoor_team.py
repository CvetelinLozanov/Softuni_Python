from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):

    ADVANTAGE_POINTS_INCREASE = 115
    BUDGET = 1000

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self.BUDGET)

    def win(self):
        self.advantage += self.ADVANTAGE_POINTS_INCREASE
        self.wins += 1