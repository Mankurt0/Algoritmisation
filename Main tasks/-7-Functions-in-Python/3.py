def triangle(a: float, b: float, c: float):
    if a + b > c and b + c > a and c + a > b:
        p = a + b + c
        s = p / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        area = round(area, 2)
        if a == b == c:
            print(f"----------------------------------------\n"
                  f"Длина сторон треугольника:  {a}, {b}, {c}\n"
                  f"----------------------------------------\n"
                  f"Информация:\n"
                  f"Равносторонний треугольник\n"
                  f"Периметр: {p}\n"
                  f"Площадь: {area}\n"
                  f"----------------------------------------")
        elif a == b or b == c or c == a:
            print(f"----------------------------------------\n"
                  f"Длина сторон треугольника:  {a}, {b}, {c}\n"
                  f"----------------------------------------\n"
                  f"Информация:\n"
                  f"Равнобедренный треугольник\n"
                  f"Периметр: {p}\n"
                  f"Площадь: {area}\n"
                  f"----------------------------------------")
        else:
            print(f"----------------------------------------\n"
                  f"Длина сторон треугольника:  {a}, {b}, {c}\n"
                  f"----------------------------------------\n"
                  f"Информация:\n"
                  f"Разносторонний треугольник\n"
                  f"Периметр: {p}\n"
                  f"Площадь: {area}\n"
                  f"----------------------------------------")
    else:
        print("Некорректные стороны. Невозможно построить треугольник.")


triangle(15, 15, 15)  #97.42785792574935
triangle(15, 20, 15)  #111.80339887498948
triangle(15, 20, 25)  #150.0
triangle(1, 2, 3)