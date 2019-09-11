def star(n):
    for i in range(n):
        t.forward(200)
        t.left(180 - 180 / n)

import turtle
t = turtle.Turtle()

star(5)
t.penup()
t.backward(300)
t.pendown()
star(11)