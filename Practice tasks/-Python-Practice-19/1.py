import urllib.request, webbrowser

try: urllib.request.urlopen("https://google.com")
except IOError:
    print("error")
else:
    user = input("Введите запрос: ")
    while True:
        user1 = input("Выбор браузера\n[1] - Google [2] - Yandex\n")
        if user1 == "1":
            webbrowser.open("https://www.google.com/search?q="+user)
            break
        elif user1 == "2":
            webbrowser.open("https://ya.ru/search/?text="+user)
            break
        else:
            print("Неверный запрос")