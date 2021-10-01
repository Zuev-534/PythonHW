import turtle
import math

turtle.shape('turtle')
turtle.speed(100)

R= 100
n= 12

for i in range(n):
    turtle.circle(R)
    turtle.left(360/n)

turtle.done()