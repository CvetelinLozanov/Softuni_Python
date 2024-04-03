from math import ceil


class sequence_repeat:
    def __init__(self, text: str, number: int):
        self.text = self.generate_text(text, number)
        self.number = number
        self.start = 0

    def generate_text(self, text: str, number: int):
        if len(text) >= number:
            return text

        word_repeat = ceil(number / len(text))
        text = text * word_repeat
        return text

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.number:
            raise StopIteration

        index = self.start
        self.start += 1
        return self.text[index]


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')