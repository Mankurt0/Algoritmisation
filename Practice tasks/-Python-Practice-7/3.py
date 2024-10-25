bin_sy = ["11011111", "11011101", "11000111", "11011100", "11011110"]
dec_sy = []
for bin in bin_sy:
    dec = 0
    j = 0
    for i in range(len(bin) - 1, -1, -1):
        dec += int(bin[i]) * (2 ** j)
        j += 1
    dec_sy.append(dec)
print(dec_sy)
print(max(dec_sy))
print(min(dec_sy))
