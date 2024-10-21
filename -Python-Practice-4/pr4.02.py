# Вариант 6
user = int(input("Введите число: "))
if user % 2 == 0:
    print(user ** 2)
elif user % 3 == 0:
    print(user ** 3)
else:
    print(user * 100)
