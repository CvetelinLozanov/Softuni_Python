from project.supply.supply import Supply
from project.supply.food import Food
from project.supply.drink import Drink
from project.player import Player
from typing import List


class Controller:
    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)

        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):
        pass

    def sustain(self, player_name: str, sustenance_type: str):
        pass

    def duel(self, first_player_name: str, second_player_name: str):
        pass

    def next_day(self):
        pass

    def __str__(self):
        result = ''
        for p in self.players:
            result += str(p) + '\n'

        for s in self.supplies:
            result += s.details() + '\n'

        return result.strip()

    def _get_existing_names(self):
        return [p.name for p in self.players]