def prime_check(x: int) -> bool:
    """
    Проводит тест простоты числа перебором.

    Параметры:
    x (int) - целое число

    Возвращает:
    True - если число простое
    False - если число не простое (включая отрицательные числа и нуль)

    Пример:
    >> prime_check(13)
    True
    >> prime_check(-1)
    False
    """
    if x < 2:  # Обработка исключений цикла
        return False

    i = 2
    while i < x:  # Тест простоты числа перебором
        if x % i != 0:
            i += 1
        else:
            return False
    else:
        return True


print(prime_check.__doc__)
print(prime_check(13))
print(prime_check(-1))
print(prime_check(103))
print(prime_check(2048))
