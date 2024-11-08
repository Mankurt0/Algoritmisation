def create_list(len: int, num: int) -> list:
    out = []
    for i in range(len):
        out.append(num)
    return out


print(create_list(5, 3))
