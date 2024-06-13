from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self):
        result = f'{self.name} Secondary Service:\n'
        robots = 'none' if not self.robots else ' '.join([robot.name for robot in self.robots])
        result += f"Robots: {robots}"
        return result.strip()
