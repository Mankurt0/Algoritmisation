while True:
    x = int(input("Введите число от 1 до 9: "))
    if 0 <= x <=9:
        for i in range(1,11):
            print(x,"*",i,"=",x*i)
        else:
            break
    else:
        print("Число вне диапазона. Попробуйте снова.")