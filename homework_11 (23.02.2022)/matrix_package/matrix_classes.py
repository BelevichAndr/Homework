from random import randint


class Matrix:
    def __init__(self, data=None, n=5, m=5, a=0, b=0):
        self.data = data
        self.n = n
        self.m = m
        self.a = a
        self.b = b

        if self.data is None:
            self.data = []
            for _ in range(n):
                strings = [randint(self.a, self.b) for _ in range(m)]
                self.data.append(strings)

    def __str__(self):
        return "\n".join([' '.join([str(element) for element in string]) for string in self.data])

    def __getitem__(self, index):
        return self.data[index]
