stations = ["Малиновка", "Рябиновка", "Суслово", "Дрожжино", "Звягино"]
for i in stations:  # range(len(stations)):
    if i == stations[-1]:
        print("Поезд на станции:", i, "конечная!")
    else:
        print("Поезд на станции:", i)
