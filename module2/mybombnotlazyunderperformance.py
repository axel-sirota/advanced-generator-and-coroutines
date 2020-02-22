class MyNotLazyBomb:

    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return MyNotLazyBombIterator(self.number)


class MyNotLazyBombIterator:

    def __init__(self, number):
        self.number = number
        self.squares = [x ** 2 for x in range(number)]  # To make next fast, we use RAM
        self.index = 0

    def __next__(self):
        if self.index >= len(self.squares):
            raise StopIteration
        value = self.squares[self.index]
        self.index += 1
        return value
