from random import randint

print("Начало игры. [a]-налево, [w]-прямо, [d]-направо.", end=" ")
ca = 0
cw = 0
cd = 0
while True:
    while True:
        user = input("Куда идти?: ")
        if user == "a":
            print("Повернул налево.", end=" ")
            ca += 1
            break
        elif user == "d":
            print("Повернул направо.", end=" ")
            cd += 1
            break
        elif user == "w":
            print("Пошёл прямо.", end=" ")
            cw += 1
            break
        else:
            print("Неправильная кнопка!")
    rand = randint(1, 10)
    if rand == 10:
        print(
            f"Выход найден! Ты выиграл! Для того, чтобы найти выход ты {ca} раз повернул налево, {cw} раз пошёл прямо и {cd} раз повернул направо.")
        break
    else:
        print("Выхода пока нет...", end=" ")
