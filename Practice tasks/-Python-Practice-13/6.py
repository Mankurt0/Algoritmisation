def exam(string: str, letter: str) -> int:
    n = 0
    for i in string:
        if i.capitalize() == letter.capitalize():
            n += 1
    return n


print(exam("My name is Sara.", "s"))
