def func(a: int) -> int:
    return a + 1


a = (func, 2)
b = a[0]
c = a[1]

print(b(c))
