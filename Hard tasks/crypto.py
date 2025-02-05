from cryptography.fernet import Fernet

aes = Fernet(Fernet.generate_key())
user = input("Введите сообщение для шифровки: ").encode()
enc = aes.encrypt(user)
print(f"Зашифрованное сообщение: {enc}")
print(f"Расшифрованое сообщение: {aes.decrypt(enc).decode()}")
