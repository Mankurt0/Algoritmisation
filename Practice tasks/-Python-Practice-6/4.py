random_elements = [["toy", "bee", "cheese", "ear"],
                   [False, "word", "0110110", 10],
                   ["happiness", "(ノ ゜Д゜)ノ ︵ ┻━┻", "luck", None],
                   ["car", "<- code ->", 4.7, True]]
answer = []
for row in random_elements:
    for i, element in enumerate(row):
        if i % 2 == 0:
            answer.append(element)
print(answer)
