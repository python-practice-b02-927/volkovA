def square(a):
    for j in range (4):
        t.forward(a)
        t.left(90)



import turtle
t = turtle.Turtle()
for i in range (1,11,1):
    square(20*i)
    t.penup()
    t.right(135)
    t.forward(14)
    t.left(135)
    t.pendown()