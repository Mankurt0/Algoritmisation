list1 = []
while len(list1) < 5:
    try:
        list1.append(int(input("Введите число: ")))
    except ValueError:
        print("Не число")
        continue
print(f"Числа в списке: {list1}")
