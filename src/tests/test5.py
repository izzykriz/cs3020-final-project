class Point:
    x: int
    y: int

    def sum(self: Point) -> int:
        return self.x + self.y


test = Point(1, 2)
z = test.sum()
print(z)
