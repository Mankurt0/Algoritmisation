notebook = {}
while True:
    key = ""
    val = ""
    keys = []
    for i in notebook:
        keys.append(i)
    print("[1] - Создать запись. [2] - Прочесть запись. [3] - Удалить  запись. [4] - Выход.")
    user = input()
    if user == "1":
        key = input("Введите название записи: ")
        val = input(f"Введите запись {key}\n")
        notebook[key] = val
    elif user == "2":
        key = input(f"Какую запись прочесть: {keys}\n")
        if key in keys:
            print(notebook[key])
        else:
            print("Неверное название записи")
    elif user == "3":
        key = input(f"Какую запись удалить: {keys}\n")
        if key in keys:
            notebook.pop(key)
        else:
            print("Неверное название записи")
    elif user == "4":
        break
    else:
        print("Неверный ввод!")
    keys.clear()