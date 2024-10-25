def create_car(name: str, color: str, speed: int) -> str:
    return f"Марка: {name} Цвет: {color} Максимальная скорость: {speed}"


car1 = create_car("Лада", "Серый", 120)
car2 = create_car("Тойота", "Красный", 300)

print(car1)
print(car2)
