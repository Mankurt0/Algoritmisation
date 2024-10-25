price = int(input("Введите цену: "))
if price > 5000:
    price *= 0.90
elif price > 1000:
    price *= 0.95
print("Итоговая сумма: ", price)