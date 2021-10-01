import turtle
import math

turtle.shape('turtle')
turtle.speed(100)


def starchen(n):
	for i in range(1,n+1):
	    turtle.forward(R)
	    turtle.left(180-180/n)
	    
N=15
R=200
starchen(N)

turtle.penup()
turtle.forward(-300)
turtle.left(180)
turtle.pendown()

starchen(N-10)

turtle.done()