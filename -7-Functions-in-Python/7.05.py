player = 0


def info_player():
    print(f"Игрок пробежал {player} км.")


def run_player(km):
    global player
    player += km / 2


info_player()
run_player(30)
run_player(12.5)
info_player()
