class Point:
    x: int
    y: int

    def sum(self):
        return self.x + self.y


test = Point(1, 2)
z = test.sum()
