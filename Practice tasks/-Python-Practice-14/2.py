list1 = [4, 43.5, 1.5, 31, 588, 320.1, 192.16]
for i, e in enumerate(list1):
    try:
        print(f"{e} / {i} = {e / i}")
    except ZeroDivisionError:
        print(f"Деление на ноль! Элемент: {e}")
