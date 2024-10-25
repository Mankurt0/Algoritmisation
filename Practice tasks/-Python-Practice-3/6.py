ticket = input("Введите номер билета: ")
a = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
b = int(ticket[-1]) + int(ticket[-2]) + int(ticket[-3])
if a == b:
    print("Счастливый")
else:
    print("Не счастливый")