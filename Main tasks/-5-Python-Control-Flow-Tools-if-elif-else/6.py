x = input("Выберите ячейку: ")
if x == "B1" or x == "B3" or x == "B7" or x == "C1" or x == "C4" or x == "C5" or x == "C6" or x == "C8" or x == "C9":
    print("В данном квадрате обитает синий попугай.")
elif x == "B2" or x == "B4" or x == "B6" or x == "B8" or x == "C2" or x == "C7" or x == "C10" or x == "C11":
    print("В данном квадрате обитает зелёный попугай.")
else:
    print("Данный квадрат пустой.")