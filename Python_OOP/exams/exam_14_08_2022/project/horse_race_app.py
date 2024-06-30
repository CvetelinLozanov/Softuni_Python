from project.jockey import Jockey
from project.horse_specification.horse import Horse
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.horse_race import HorseRace
from typing import List


class HorseRaceApp:

    HORSES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type in self.HORSES:
            horse = self._get_horse(horse_name)
            if horse:
                raise Exception(f"Horse {horse_name} has been already added!")

            self.horses.append(self.HORSES[horse_type](horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        existing_jockey = self._get_jockey(jockey_name)

        if existing_jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        current_races = [race.race_type for race in self.horse_races]
        if race_type in current_races:
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self._get_jockey(jockey_name)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse = self._get_last_horse(horse_type)

        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self._get_horse_race(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self._get_jockey(jockey_name)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self._get_horse_race(race_type)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = sorted(race.jockeys, key=lambda j: -j.horse.max_speed)[0]

        return (f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}!"
                f" Winner's horse: {winner.horse.name}.")

    def _get_horse(self, horse_name: str):
        return next((horse for horse in self.horses if horse.name == horse_name), None)

    def _get_jockey(self, jockey_name: str):
        return next((jockey for jockey in self.jockeys if jockey.name == jockey_name), None)

    def _get_last_horse(self, horse_type: str):
        horse = [horse for horse in self.horses if horse.__class__.__name__ == horse_type and not horse.is_taken]
        return horse[-1] if horse else None

    def _get_horse_race(self, race_type):
        horse_race = [race for race in self.horse_races if race.race_type == race_type]
        return horse_race[0] if horse_race else None
