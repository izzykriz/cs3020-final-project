class Object1:
    def __init__(self, n: int):
        self.n = n

    def func(self):
        return self.n * self.n


class Object2(Object1):
    def __init__(self, n: int):
        super().__init__(n)

    def func(self):
        return self.n * self.n * self.n


o1 = Object1(2)
o2 = Object2(2)
print(o1.func())
print(o2.func())
