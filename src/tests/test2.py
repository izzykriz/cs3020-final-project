class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def add_points(a: Point, b: Point) -> Point:
    return Point(a.x + b.x, a.y, b.y)


print(add_points(Point(1, 1), Point(3, -2)))
