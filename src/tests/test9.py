class Shape:
    area: int

    def get_area(self: Shape) -> int:
        return self.area


class Square(Shape):
    side_len: int

    def get_side_len(self: Square) -> int:
        return self.side_len


sq = Square(4, 2)

print(sq.get_area())
print(sq.get_side_len())
