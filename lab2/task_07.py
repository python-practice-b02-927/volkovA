
import math
import turtle
t = turtle.Turtle()

k =5
delta_l = 8
phi = 0
for i in range(400):
    r = k*phi 
    delta_phi = delta_l / (k+r)
    t.left(180*delta_phi / math.pi)
    phi += delta_phi
    t.forward(delta_l)
