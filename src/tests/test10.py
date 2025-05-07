def func(a: int) -> int:
    return a + 1


b = (func, 2)

print(b[0](b[1]))
