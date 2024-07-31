from typing import List

from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:
    def __init__(self):
        self.decorations: List[BaseDecoration] = []

    def add(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True

        return False

    def find_by_type(self, decoration_type: str):
        decoration = self.__find_first_decoration_from_type(decoration_type)
        return decoration

    def __find_first_decoration_from_type(self, decoration_type: str):
        decoration = [d for d in self.decorations if d.__class__.__name__ == decoration_type]
        return decoration[0] if decoration else "None"
