def alpha(inp: str):
    inp = list(inp)
    abc = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    out = []
    for i in inp:
        if i in abc:
            out.append(i)
            abc.remove(i)
    out += abc
    return out


print(alpha("пайтон"))
