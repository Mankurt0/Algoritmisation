def isint(var):
    if type(var) == type(1):
        return True
    else:
        return False


class Book:
    def __init__(self, name: str, pages: int, year: int):
        self.name = name
        self.pages = pages
        self.year = year

    def info(self):
        print(f"Название: {self.name}\nКоличество страниц: {self.pages}\nГод издания: {self.year}\n")

    def update_pages(self, pages: int):
        if isint(pages):
            self.pages = pages
        else:
            print("Неверное значение страниц\n")

    def older_than(self, year: int):
        if isint(year):
            if self.year > year:
                print(True)
            else:
                print(False)
        else:
            print("Неверное значение года\n")


book1 = Book("Name1", 200, 2005)
book2 = Book("Name2", 500, 1999)
book1.info()
book1.update_pages(250)
book1.info()
book2.older_than(2000)
