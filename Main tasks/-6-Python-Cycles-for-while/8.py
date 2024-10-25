while True:
    x = input()
    if x == "w":
        print("Персонаж  идёт прямо")
    elif x == "a":
        print("Персонаж  идёт влево")
    elif x == "s":
        print("Персонаж  идёт назад")
    elif x == "d":
        print("Персонаж  идёт вправо")
    elif x == "stop":
        break
    else:
        print("Неизвестная команда")
print("Программа остановлена")