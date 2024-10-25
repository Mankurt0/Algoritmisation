# Вариант 6
user1 = int(input("Введите первое число: "))
user2 = int(input("Введите второе число: "))
if user1 >= 0 and user2 >= 0:
    print(True)
elif user1 < 0 and user2 < 0:
    print(False)
elif user1 < 0:
    print(user1 + 1000, user2)
elif user2 < 0:
    print(user1, user2 + 1000)
