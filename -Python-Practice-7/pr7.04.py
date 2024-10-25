matrix = [[-446, 281, -80],
          [465, 432, -122],
          [13, "error", 8]]
matrix_sum = 0
for row in matrix:
    for i, elem in enumerate(row):
        if isinstance(elem, str):
            row[i] = len(elem)
        matrix_sum += row[i]
print(matrix)
print(matrix_sum)
