def star(lst: list, row: int, elem: int):
    lst[row][elem] = " * "
    print(lst[0])
    print(lst[1])
    print(lst[2])


field = [["[ ]", "[ ]", "[ ]"],
         ["[ ]", "[ ]", "[ ]"],
         ["[ ]", "[ ]", "[ ]"]]
star(field, 2, 1)
