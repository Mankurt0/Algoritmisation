n = int(input("Введите число n: "))
k = int(input("Введите число k: "))
if n % k == 0:
    print(n,"кратно",k)
else:
    print(n,"не кратно",k)