def line(number):
    t.forward(100)
    t.stamp()
    t.left(180)
    t.forward(100)
    t.right(180 - 360 / number)
    
    
import turtle
t = turtle.Turtle()

n = 9
 
for i in range (n):
    line(n)
t.hideturtle()
