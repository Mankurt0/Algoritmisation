matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nc = []
c = 0
print("matrix:")
for a in matrix:
    print(a)
for r in matrix:
    for e in r:
        if e % 2 != 0:
            nc.append(e)
        else:
            c += 1
print(f"Нечётные числа matrix:\n{nc}")
print(f"Количество чётных: {c}")
