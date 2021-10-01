import turtle
import math

s = 0
R = 200
a = 3.15*R/180

turtle.shape('turtle')
turtle.speed(100)
turtle.penup()
turtle.forward(R)
turtle.pendown()

turtle.left(90)
for i in range(400):
	turtle.left(180/R)
	turtle.forward(a)

turtle.done()