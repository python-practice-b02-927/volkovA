def arc(r, phi):
    for i in range(int(phi / 3)):
        t.forward(3 * math.pi / 180 * r)
        t.right(3)

import turtle
t = turtle.Turtle()
import math

t.left(90)
for i in range(10):
    arc(100,180)
    arc(20,180)

