text = str(input("Введите текстовое сообщение: "))
save = input("Хотите ли вы сохранить это сообщение?(yes/no): ")
if save == 'yes':
    path = input('Введите имя файла, в котором сохранится ваше сообщение: ')
    with open(path, "w") as file:
        file.write(f"{text}")
else:
    print('no save')
