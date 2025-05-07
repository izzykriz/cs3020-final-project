class Point:
    x: int
    y: int

    def add1x(self: Point) -> int:
        return self.x + 1


a = Point(5, 6)
b = Point(1, 2)
print(a.add1x())
print(b.add1x())