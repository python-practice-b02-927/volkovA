def circle(r):
    for i in range (100):
        t.forward(math.pi *r / 100)
        t.left(360 / 100)

import turtle
t = turtle.Turtle()
import math

for j in range(6):
    circle(200)
    t.left(60)
t.hideturtle()