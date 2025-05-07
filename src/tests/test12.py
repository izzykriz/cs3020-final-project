class Number:
    val: int

    def set_num(self: Number, new: int) -> Number:
        self.val = new
        return self


n = Number(4)
print(n.val)
n = n.set_num(5)
print(n.val)
