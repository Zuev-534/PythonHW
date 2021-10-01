import turtle
import math

turtle.shape('turtle')
turtle.speed(100)

PI = 3.14159265359
N = 10

def Rad(F):
	turtle.penup()
	turtle.forward(F)
	turtle.pendown()

def Ugolnik(n):
	R = 10*n 
	a = R*(2*(math.sin(PI/n))) 
	Ug = 180 - (180*2)/n
	Rad(R)
	turtle.left(Ug/2)
	for i in range(1, n+1):
		turtle.left(180-Ug)
		turtle.forward(a)
	turtle.left(-Ug/2)
	Rad(-R)

for z in range(3, N):
	Ugolnik(z)

turtle.done()