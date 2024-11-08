def cust_filter(inp: list) -> bool:
    summ = 0
    for i in inp:
        if isinstance(i, int) and i % 7 == 0:
            summ += i
    if summ < 83:
        return True
    else:
        return False


print(cust_filter([7, 10.5, "txt", 14, 2, 56]))
