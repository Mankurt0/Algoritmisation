def punct(txt: str) -> int:
    a = "!?.,()"
    out = 0
    for i in txt:
        if i in a:
            out += 1
    return out


print(punct("(Как дела, друг?)"))
