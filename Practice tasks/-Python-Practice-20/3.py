import datetime


def add(x: str):
    y = datetime.datetime.now()
    with open("log note.txt", "a") as file:
        file.write(f"{y}: {x}\n")


add("Запись")
