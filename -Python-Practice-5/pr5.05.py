pos = []
neg = []
zer = []
out1 = 0
out2 = 0
out3 = 0
num = int(input("Введите количество чисел: "))
for i in range(num):
    a = float(input("Введите число: "))
    if a > 0:
        pos.append(a)
    elif a < 0:
        neg.append(a)
    else:
        zer.append(a)
for i in neg:
    out1 += i
for i in pos:
    out2 += i
if len(pos) != 0:
    out2 = out2 / len(pos)
else:
    out2 = 0
out3 = list("*" * len(zer))
print(out1)
print(out2)
print(f"Количество звёзд: {len(zer)} {out3}")
