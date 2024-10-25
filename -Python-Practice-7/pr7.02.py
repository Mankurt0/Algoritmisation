word_numb = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
user = int(input("Введите число от 0 до 9: "))
if user < 0 or user > 9:
    print("Неверное число")
    quit()
for i in range(user + 1):
    print(word_numb[i])
