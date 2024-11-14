def bin_sys(a: int, b: int):
    n = b - a + 1
    sumout = 0
    for i in range(n):
        out = bin(i + a)
        sumout += i + a
        out = out[2::]
        print(out)
    sumout = bin(sumout)[2::]
    print(f"Сумма: {sumout}")


bin_sys(3, 6)
