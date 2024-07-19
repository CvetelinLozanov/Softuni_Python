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
        self.supplies.extend(supplies)

    # def sustain(self, player_name: str, sustenance_type: str):
    #     supply = self._get_last_supply(sustenance_type)
    #     player = self._find_player(player_name)
    #
    #     if not player.need_sustenance:
    #         return f"{player_name} have enough stamina."
    #
    #     if sustenance_type == 'Food' and not supply:
    #         return 'There are no food supplies left!'
    #
    #     if sustenance_type == 'Drink' and not supply:
    #         return 'There are no drink supplies left!'
    #
    #     if supply:
    #         player.sustaining(supply.energy)
    #         return f'{player_name} sustained successfully with {supply.name}.'

    def sustain(self, player_name: str, sustenance_type: str):
        player = self._find_player(player_name)
        if player.stamina == 100:
            return f"{player.name} have enough stamina."
        supply = self._get_last_supply(sustenance_type)
        if supply:
            player.sustaining(supply.energy)
            return f"{player_name} sustained successfully with {supply.name}."

    @staticmethod
    def __attack(p1, p2):
        p2.stamina -= (p1.stamina / 2)
        if p1.stamina - (p2.stamina / 2) < 0:
            p1.stamina = 0
        else:
            p1.stamina -= (p2.stamina / 2)
        if p1 < p2:
            return f"Winner: {p2.name}"
        else:
            return f"Winner: {p1.name}"

    @staticmethod
    def __check_if_the_players_cannot_duel(*players):
        result = []
        for player in players:
            if player.stamina == 0:
                result.append(f"Player {player.name} does not have enough stamina.")
        if result:
            return '\n'.join(result)

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self._find_player(first_player_name)
        second_player = self._find_player(second_player_name)

        result = self.__check_if_the_players_cannot_duel(first_player, second_player)
        if result:
            return result

        if first_player < second_player:
            return self.__attack(first_player, second_player)
        else:
            return self.__attack(second_player, first_player)

    def next_day(self):
        for player in self.players:

            if player.stamina - player.age * 2 < 0:
                player.stamina = 0
            else:
                player.stamina -= (player.age * 2)

        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ''
        for p in self.players:
            result += str(p) + '\n'

        for s in self.supplies:
            result += s.details() + '\n'

        return result.strip()

    def _find_player(self, player_name: str):
        return next((p for p in self.players if p.name == player_name), None)

    def _get_last_supply(self, supply_type):
        for index in range(len(self.supplies) - 1, -1, -1):
            if supply_type == self.supplies[index].__class__.__name__:
                return self.supplies.pop(index)
