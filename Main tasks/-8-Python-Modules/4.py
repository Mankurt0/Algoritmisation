import random
import colorama

colorama.init(autoreset=True)
number = random.randint(0, 10)
c = 0
print("Число сгенерировано")
while True:
    user = int(input("Угадайте число: "))
    if 0 <= user <= 10:
        if user > number:
            print(colorama.Fore.RED + "Ваше число больше")
        elif user < number:
            print(colorama.Fore.RED + "Ваше число меньше")
        else:
            print(colorama.Fore.GREEN + "Вы угадали!")
            break
        c += 1
    else:
        print(colorama.Fore.RED + "Введите число от 1 до 10!")
print(f"Попыток было: {c}")
