class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.__start_index = len(iterable) - 1
        self.__end_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start_index < self.__end_index:
            raise StopIteration

        index = self.__start_index
        self.__start_index -= 1
        return self.iterable[index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
