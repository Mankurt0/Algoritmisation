class CreateCharacter:
    def __init__(self, character_name: str, character_class: str, character_health: int, character_damage: int):
        self.name = character_name
        self.cclass = character_class
        self.health = character_health
        self.damage = character_damage

    def info(self):
        print(f"Имя: {self.name}\nКласс: {self.cclass}\nЗдоровье: {self.health}\nУрон: {self.damage}\n")

    def trip_start(self):
        print(f"Персонаж {self.name} отправился в путешествие и пока недоступен.\n")

    def trip_end(self):
        print(f"Персонаж {self.name} возвращается назад.\n")

    def train(self):
        print(f"Персонаж {self.name} начал тренировку. Некоторое время он не будет доступен, однако станет сильнее!\n")
        self.health += 10
        self.damage += 5

    def battle(self):
        print(
            f"Персонаж {self.name} хочет начать сражаться!\nЕго показатели: Жизни: {self.health} и урон: {self.damage}\n")


pers_1 = CreateCharacter("Игорь", "Боец", 99, 15)
pers_1.info()
pers_1.trip_start()
pers_1.trip_end()
pers_1.train()
pers_1.info()
pers_1.battle()
