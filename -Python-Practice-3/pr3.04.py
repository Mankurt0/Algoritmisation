command = input("Выберите форму комнаты (прямоугольник/треугольник/круг): ")
if command == "прямоугольник":
    a = int(input("Введите длину комнаты: "))
    b = int(input("Введите ширину комнаты: "))
    s = a * b
    print(f"Площадь комнаты: {s}")
elif command == "треугольник":
    a = int(input("Введите первую сторону комнаты: "))
    b = int(input("Введите вторую сторону комнаты: "))
    c = int(input("Введите третью сторону комнаты: "))
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f"Площадь комнаты: {s}")
elif command == "круг":
    a = int(input("Введите радиус комнаты: "))
    s = a * 3.14
    print(f"Площадь комнаты: {s}")
else:
    print("Неверная команда")