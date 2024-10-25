import random

list_1 = [10, 20, 30, 40, 50]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(5):
    print(random.randint(1, 50))
print(random.choice(list_1))
random.shuffle(list_2)
print(list_2)
