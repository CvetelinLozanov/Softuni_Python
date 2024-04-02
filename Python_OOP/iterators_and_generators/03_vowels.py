class vowels:
    def __init__(self, text: str):
        self.text = text
        self.vowels = ['a', 'o', 'e', 'i', 'u', 'y']
        self.filtered_vowels = [letter for letter in self.text if letter.lower() in self.vowels]
        self.start_index = 0
        self.end_index = len(self.filtered_vowels) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_index > self.end_index:
            raise StopIteration

        index = self.start_index
        self.start_index += 1

        return self.filtered_vowels[index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)