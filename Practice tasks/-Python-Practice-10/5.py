def constructor(a: int, b: int, c: int, d: int) -> int:
    a = a // 72
    b = b // 4
    c = c // 2
    d = d // 7
    return min(a, b, c, d)


print(constructor(144, 8, 4, 14))
