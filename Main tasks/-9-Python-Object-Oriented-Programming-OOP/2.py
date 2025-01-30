class Room:

    def __init__(self, name):
        self.name = name
        self.items = []

    def print_items(self):
        print(f"Все предметы в комнате {self.name}: {', '.join(self.items)}")

    def add_item(self, *item):
        self.items.extend(item)

    def del_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Все предметы в комнате: {', '.join(self.items)}")
        else:
            print("Такого предмета нет в комнате")

    def find_item(self, item):
        if item in self.items:
            print("Такой предмет есть в комнате")
        else:
            print("Такого предмета нет в комнате")

    def count_items(self):
        print(f"В комнате {len(self.items)} предметов")

    def clear_items(self):
        self.items = []

    def replace_item(self, old_item, new_item):
        if old_item in self.items:
            self.items.remove(old_item)
            self.items.append(new_item)
            print(f"Предмет {old_item} заменён на {new_item}")
        else:
            print("Такого предмета нет в комнате")

    def move_item_to(self, item, another_room):
        if item in self.items:
            self.items.remove(item)
            another_room.items.append(item)
            print(f"Предмет {item} перенесён в {another_room.name}")
        else:
            print("Такого предмета нет в комнате")


room1 = Room("Кухня")
room2 = Room("Ванная")
room1.add_item("Холодильник", "Стул", "Стол")
room1.move_item_to("Холодильник", room2)
room1.print_items()
room2.print_items()
