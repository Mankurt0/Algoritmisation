inventory = ["яблоко", "шариковая ручка"]
if "ключ" in inventory and "фонарь" in inventory:
    print("Вы можете пройти через дверь.")
elif "ключ" not in inventory and "фонарь" in inventory:
    print("У вас нет ключа, вы не можете открыть дверь.")
elif "ключ" in inventory and "фонарь" not in inventory:
    print("У вас нет фонаря, слишком темно, чтобы пройти.")
else:
    print("У вас нет ни ключа, ни фонаря, вы не можете пройти через дверь.")
