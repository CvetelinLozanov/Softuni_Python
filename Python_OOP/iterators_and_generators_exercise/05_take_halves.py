def solution():

    def integers(n):
        # TODO: Implement
        start = 1
        end = n
        while start <= end:
            yield start
            start += 1

    def halves(n):

        for i in integers(n):
            # TODO: Implement
            yield i / 2

    def take(n, seq):
        # TODO: Implement
        pass

    return (take, halves, integers)