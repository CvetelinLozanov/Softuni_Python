from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):

    ADVANTAGE_POINTS_INCREASE = 145
    BUDGET = 500

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self.BUDGET)

    def win(self):
        self.advantage += self.ADVANTAGE_POINTS_INCREASE
        self.wins += 1
