lvl = int(input("Введите уровень: "))
hp = int(input("Введите здоровье: "))
if 5 > lvl > 0:
    print("Ваш уровень слишком низкий для выполнения миссии.")
elif 100 >= lvl >= 5:
    if 50 <= hp <= 100:
        print("Вы готовы к миссии!")
    elif 50 > hp >= 20:
        print("Ваше здоровье низкое, будьте осторожны.")
    elif 20 > hp > 0:
        print("Ваше здоровье слишком низкое для выполнения миссии.")
    else:
        pass
else:
    print("Некорректные данные.")
