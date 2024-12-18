with open("data.txt", "r") as file:
    x = file.read()
c = 0
y = x.split("\n")
for i in y:
    if 'John' in i:
        c += 1
print(c)
