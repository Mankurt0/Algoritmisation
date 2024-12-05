import turtle

colors = ["red", "blue", "green", "cyan", "magenta", "yellow"]
for i in colors:
    turtle.color(i)
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
turtle.done()