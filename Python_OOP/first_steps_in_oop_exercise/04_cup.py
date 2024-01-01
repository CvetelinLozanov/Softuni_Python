class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity_to_fill) -> int:
        if self.quantity + quantity_to_fill < self.size:
            self.quantity += quantity_to_fill
            return self.quantity

    def status(self) -> int:
        return self.size - self.quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())