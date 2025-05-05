class Object:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def add_nums(self):
        return self.a + self.b


o = Object(2, 3)
print(o.add_nums())
