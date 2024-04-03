class dictionary_iter:
    def __init__(self, dict_obj):
        self.dict_obj = dict_obj
        self.result = [(k, v) for k, v in dict_obj.items()]
        self.start = 0
        self.end = len(self.result)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration

        index = self.start
        self.start += 1
        return self.result[index]


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)