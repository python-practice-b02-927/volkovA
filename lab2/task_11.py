def circle(r):
    for i in range (50):
        t.forward(math.pi *r / 50)
        t.left(360 / 50)

import turtle
t = turtle.Turtle()
import math

for i in range(8):
    circle(100+20*i)
    t.left(180)
    circle(100+20*i)