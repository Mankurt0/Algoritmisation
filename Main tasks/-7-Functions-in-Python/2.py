def switch_check(switch: bool):
    if switch == True:
        print("True работает")
    elif switch == False:
        print("False не работает")
    else:
        print(f"{switch} сломан.")


switch_1 = True
switch_2 = False
switch_3 = None

switch_check(switch_1)
switch_check(switch_2)
switch_check(switch_3)
