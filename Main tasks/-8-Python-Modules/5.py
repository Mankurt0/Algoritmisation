import random

dice = ("|       |\n"
        "|   0   |\n"
        "|       |",

        "|0      |\n"
        "|       |\n"
        "|      0|",

        "|      0|\n"
        "|   0   |\n"
        "|0      |",

        "|0     0|\n"
        "|       |\n"
        "|0     0|",

        "|0     0|\n"
        "|   0   |\n"
        "|0     0|",

        "|0     0|\n"
        "|0     0|\n"
        "|0     0|",)

print("Добро пожаловать в игру 'Кости'!")
while True:
    print("Бот бросает кубик...")
    roll_bot = random.randint(0, 5)
    print(f"Выпало число: {roll_bot + 1}")
    print(dice[roll_bot])
    input("Ваша очередь! Нажмите Enter для броска кубика.")
    print("Вы бросаете кубик...")
    roll_user = random.randint(0, 5)
    print(f"Выпало число: {roll_user + 1}")
    print(dice[roll_user])
    if roll_user > roll_bot:
        print("Вы победили!")
        break
    elif roll_bot > roll_user:
        print("Бот победил!")
        break
    else:
        print("Ничья! Бросаем кубики снова...\n")
