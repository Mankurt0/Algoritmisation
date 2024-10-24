matrix1 = [[2, 4, 3, 6],
           [5, 7, 1, 5]]
matrix2 = [[2, 9, 0, 2],
           [3, 4, 7, 6]]
answer =  [[0, 0, 0, 0],
           [0, 0, 0, 0]]
for row in range(len(answer)):
    for elem in range(len(answer[0])):
        answer[row][elem] = matrix1[row][elem] * matrix2[row][elem]
sum1 = 0
sum2 = 0
for i in answer[0]:
    sum1 += i
for i in answer[1]:
    sum2 += i
print(f"{answer}\n{answer[0]} сумма строки: {sum1}\n{answer[1]} сумма строки: {sum2}")