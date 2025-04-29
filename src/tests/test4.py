class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Square:
    def __init__(self, center: Point, length: int):
        self.center = center
        self.length = length

    def get_area(self) -> int:
        return self.length * self.length


s = Square(Point(0, 0), 4)
print(s.get_area())
