class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.result = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration

        self.count -= 1
        result = self.result
        self.result += self.step
        return result


numbers = take_skip(2, 6)
for number in numbers:
    print(number)