from random import randint
import colorama

colorama.init(autoreset=True)
hero_name = input("Введите имя героя: ")
hero_health = 100
dragon_health = 500

while True:
    hero_damage = randint(14, 18)
    hero_crit = randint(1, 4)
    print(
        colorama.Fore.GREEN + f"\nЗдоровье {hero_name}: {hero_health}" + colorama.Fore.RED + f"\nЗдоровье дракона: {dragon_health}")
    input("\nВаш ход! Нажмите enter для удара")
    print(f"Вы атакуете дракона")
    if hero_crit == 4:
        print(colorama.Fore.BLUE + f"Критическое попадание! Вы наносите {hero_damage * 2} единиц урона")
        dragon_health -= hero_damage * 2
    else:
        print(colorama.Fore.GREEN + f"Вы наносите {hero_damage} единиц урона")
        dragon_health -= hero_damage
    if dragon_health <= 0:
        victory = True
        break

    dragon_damage = randint(8, 12)
    dragon_hit = randint(1, 4)
    print(
        colorama.Fore.GREEN + f"\nЗдоровье {hero_name}: {hero_health}" + colorama.Fore.RED + f"\nЗдоровье дракона: {dragon_health}")
    input("\nХод дракона! Нажмите enter для продолжения")
    print("Дракон атакует вас")
    if dragon_hit == 4:
        print(colorama.Fore.RED + f"Дракон попал по вам и нанёс {dragon_damage} единиц урона!")
        hero_health -= dragon_damage
    else:
        print(colorama.Fore.YELLOW + "Дракон не попал по вам")
    if hero_health <= 0:
        victory = False
        break

if victory:
    print(colorama.Fore.GREEN + "\nВы победили!")
else:
    print(colorama.Fore.RED + "\nВы проиграли")
