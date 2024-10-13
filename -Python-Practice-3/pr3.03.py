a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
p = (a+b+c)/2
s = (p*(p-a)*(p-b)*(p-c))**0.5
print(f"Площадь треугольника: {s}")