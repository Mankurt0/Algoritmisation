a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Выберите операцию:\n1: +\n2: -\n3: *\n4: /\n"))
if c == 1:
    print("Ответ: ",a+b)
elif c == 2:
    print("Ответ: ",a-b)
elif c == 3:
    print("Ответ: ",a*b)
elif c == 4:
    print("Ответ: ",a/b)
else:
    print("Неверная операция")