minutes = int(input("Введите количество минут: "))
hours = minutes // 60
minutes = minutes % 60
print(f"{hours} часов {minutes} минут")