fruits = [["Banana", "apple"], ["apricot", "Avocado"], ["lime", "lemon"], ["Mango", "grapes"]]
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = []
for row in fruits:
    for element in row:
        if element[0] in upper:
            answer.append(element)
print(answer)
