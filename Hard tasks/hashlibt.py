import hashlib

user = input("Введите строку для хеширования: ").encode()
hash = hashlib.sha256()
hash.update(user)
print(f"Хеш sha256 для введённой строки: {hash.digest()}")
