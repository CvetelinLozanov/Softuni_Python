from project.room import Room
from typing import List


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people):
        room = [room for room in self.rooms if room.number == room_number][0]
        return room.take_room(people)

    def free_room(self, room_number: int):
        room = [room for room in self.rooms if room.number == room_number][0]
        if room:
            return room.free_room()

    def status(self):
        guests = sum([room.guests for room in self.rooms])
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        return (f'Hotel {self.name} has {guests} total guests\n'
                f'Free rooms: {", ".join(free_rooms)}\n'
                f'Taken rooms: {", ".join(taken_rooms)}')
