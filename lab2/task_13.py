def circle(r):
    for i in range (50):
        t.forward(math.pi *r / 50)
        t.right(360 / 50)

def eye():
    t.pendown()
    t.color('black','blue')
    t.begin_fill()
    circle(50)
    t.end_fill()
    t.penup()
    
def arc(r, phi):
    for i in range(int(phi / 3)):
        t.forward(3 * math.pi / 180 * r)
        t.right(3)

import turtle
t = turtle.Turtle()
import math

t.color('black','yellow')
t.goto(-10, 270)
t.begin_fill()
circle(400)
t.end_fill()
t.penup()
t.goto(80, 180)
eye()
t.goto(-80,180)
eye()
t.goto(0, 100)
t.right(90)
t.pendown()
t.pensize(8)
t.color('black')
t.forward(70)
t.penup()
t.goto(100,20)
t.right(20)
t.pendown()
t.color('red')
arc(100,140)

