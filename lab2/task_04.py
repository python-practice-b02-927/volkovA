import turtle

t = turtle.Turtle()

n = 100
for i in range (n):
    t.forward(1000 / n)
    t.left(360 / n)
    