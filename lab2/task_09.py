def polygone(R,n):
    a = 2*R * math.sin(math.pi / n)
    for i in range(n):
        t.forward(a)
        t.left(360 / n)
            

import turtle
import math
t = turtle.Turtle()

R = 30
t.penup()
t.left(30)
t.backward(30)
t.right(30)
t.pendown()
for j in range(3,15):
    polygone(R,j)
    R += 30
    t.penup()
    t.left(90 - 180 / j)
    t.backward(30)
    t.right(90 - 180 / (j+1))
    t.pendown()
    
 
    
  