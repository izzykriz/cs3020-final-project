class Point:
    x: int
    y: int

    def add1(self: Point) -> int:
        return self.x + 1


class Book:
    name: bool

    def get_name(self: Book) -> bool:
        return self.name


a = Point(5, 6)
b = Book(True)
print(a.add1())
print(b.get_name())
