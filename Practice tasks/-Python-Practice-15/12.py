import turtle
turtle.setheading(90)
step_total = 0
while True:
    wasd = turtle.textinput("Куда" ,"Куда")
    step = turtle.numinput("Сколько", "Сколько")
    if wasd == "w":
        turtle.forward(step)
    elif wasd == "a":
        turtle.left(90)
        turtle.forward(step)
    elif wasd == "s":
        turtle.left(180)
        turtle.forward(step)
    elif wasd == "d":
        turtle.right(90)
        turtle.forward(step)
    elif wasd == "exit":
        break
    step_total += step
turtle.write(f"Всего сделано {step_total} шагов")
turtle.done()