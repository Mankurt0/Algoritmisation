while True:
    x = input("Введите число: ")
    try:
        x = int(x)
    except ValueError:
        print(f"{x} - не число. Повторите ввод.")
    else:
        break
for i in range(x + 1):
    print(i, end=" ")
