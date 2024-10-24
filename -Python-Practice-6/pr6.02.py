matrix1 = [[2, 4, 3, 6],
           [5, 7, 1, 5]]
matrix2 = [[2, 9, 0, 2],
           [3, 4, 7, 6]]
answer =  [[0, 0, 0, 0],
           [0, 0, 0, 0]]
for row in range(len(answer)):
    for elem in range(len(answer[0])):
        answer[row][elem] = matrix1[row][elem] * matrix2[row][elem]
x = answer[0]
b = 0
for a in x:
    b += a
print(b)