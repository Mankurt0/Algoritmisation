n = int(input("Введите n: "))
n = n % 100
if n % 10 == 1 and n != 11:
    print(f"{n} программист")
elif (n % 10 == 2 or n % 10 == 3 or n % 10 == 4) and (n != 12 or n != 13 or n != 14):
    print(f"{n} программиста")
else:
    print(f"{n} программистов")