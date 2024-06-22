from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band import Band
from project.concert import Concert
from typing import List


class ConcertTrackerApp:
    MUSICIANS = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.MUSICIANS:
            raise ValueError("Invalid musician type!")

        musician = self._get_musician(name)

        if musician:
            raise Exception(f"{name} is already a musician!")

        self.musicians.append(self.MUSICIANS[musician_type](name, age))
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = self._get_band(name)

        if band:
            raise Exception(f"{name} band is already created!")

        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self._get_concert(place)

        if concert:
            raise Exception(f"{place} is already registered for {genre} concert!")

        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self._get_musician(musician_name)
        band = self._get_band(band_name)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self._get_band(band_name)

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = self._get_musician_from_band(band, musician_name)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)

    def start_concert(self, concert_place: str, band_name: str):
        concert = self._get_concert(concert_place)
        band = self._get_band(band_name)

        drummers = []
        singers = []
        guitarists = []

        for member in band.members:
            if member.__class__.__name__ == 'Guitarist':
                guitarists.append(member)
            elif member.__class__.__name__ == 'Drummer':
                drummers.append(member)
            elif member.__class__.__name__ == 'Singer':
                singers.append(member)

        if len(drummers) < 1 and len(guitarists) < 1 and len(singers) < 1:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == 'Rock':
            if all("play the drums with drumsticks" not in drummer.skills for drummer in drummers) \
                    or all("sing high pitch notes" not in singer.skills for singer in singers) \
                    or all("play rock" not in guitarist.skills for guitarist in guitarists):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        if concert.genre == 'Metal':
            if all("play the drums with drumsticks" not in drummer.skills for drummer in drummers) \
                    or all("sing low pitch notes" not in singer.skills for singer in singers) \
                    or all("play metal" not in guitarist.skills for guitarist in guitarists):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        if concert.genre == 'Jazz':
            if all("play the drums with drum brushes" not in drummer.skills for drummer in drummers) \
                    or all("sing high pitch notes" and
                           "sing low pitch notes" not in singer.skills for singer in singers) \
                    or all("play jazz" not in guitarist.skills for guitarist in guitarists):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

    def _get_concert(self, place):
        concert = [concert for concert in self.concerts if concert.place == place]
        return concert[0] if concert else None

    def _get_band(self, band_name):
        band = [band for band in self.bands if band.name == band_name]
        return band[0] if band else None

    def _get_musician(self, musician_name):
        musician = [musician for musician in self.musicians if musician.name == musician_name]
        return musician[0] if musician else None

    def _get_musician_from_band(self, band, musician_name):
        musician = [member for member in band.members if member.name == musician_name]
        return musician[0] if musician else None
