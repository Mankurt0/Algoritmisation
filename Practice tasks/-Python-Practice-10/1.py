def upper(t: str) -> str:
    out = ""
    for i in t:
        if i.isupper():
            out += i
    return out


print(upper("PrIVet"))
