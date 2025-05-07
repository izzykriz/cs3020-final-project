class Shape:
    area: int


class Square(Shape):
    side_len: int


sq = Square(4, 2)

print(sq.area)
print(sq.side_len)
