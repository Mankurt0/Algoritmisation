all_d = {1: 15, 4: 80, 44: 0, 256: 15, 100: 70, 101: 70, 20: 444, 3: 9}
print(all_d)
key = (1, 101, 3)
for i in key:
    all_d.pop(i)
print(all_d)
