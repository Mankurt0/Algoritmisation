def calendar(name: str, year: int, days: int):
    print(f"Календарь: {name} {year}")
    for i in range(days):
        if (i + 1) % 7 == 0:
            print(i + 1, end="\n")
        else:
            print(i + 1, end=" ")


calendar("Гойдябрь", 2077, 36)
