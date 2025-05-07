class Point:
    x: int
    y: int


class Circle:
    center: Point
    radius: int


c = Circle(Point(1, 2), 5)

print(c.center.x)
print(c.center.y)
