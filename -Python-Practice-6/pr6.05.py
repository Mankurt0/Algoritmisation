row_number = int(input("Введите число строк: "))
ele_number = int(input("Введите число столбцов: "))
matrix = []
for row in range(row_number):
    matrix.append([])
    for ele in range(ele_number):
        matrix[row].append(0)
        matrix[row][ele] = int(input(f"Введите значение элемента [{row}][{ele}]: "))
print(f"Ваш двумерный массив:\n{matrix}")
