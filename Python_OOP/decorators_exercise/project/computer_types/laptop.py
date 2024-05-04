from project.computer_types.computer import Computer

class Laptop(Computer):

    def __init__(self, processor: str, model: str):
        super().__init__(processor, model)


    @property
    def _valid_processors(self):
        return {"AMD Ryzen 9 5950X": 900,
         "Intel Core i9-11900H": 1050,
         "Apple M1 Pro": 1200}

    @property
    def _valid_ram(self):
        return {2 ** pow: pow for pow in range(1, 7)}

    @property
    def _type(self):
        return 'laptop'