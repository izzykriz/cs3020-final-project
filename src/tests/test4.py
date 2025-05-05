class Point:
    x: int
    y: int

    def sum(self: Point) -> int:
        return self.x + self.y


p = Point(3, 3)
print(p.sum())
