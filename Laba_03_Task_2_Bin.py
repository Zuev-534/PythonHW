from random import *
import turtle

turtle.shape('turtle')
turtle.speed(100)
L= 10
Lr=L
Ld=L*2**0.5

def Chislo(x):
	if x == 0 :
		for i in range(1,3):
			for j in range(1,3):
				turtle.forward(j*Lr)
				turtle.right(90)
		turtle.penup()
		turtle.forward(2*Lr)
		turtle.pendown()
	else :
		turtle.penup()
		turtle.right(90)
		turtle.forward(Lr)
		turtle.pendown()
		turtle.left(135)
		turtle.forward(Ld)
		turtle.right(135)
		turtle.forward(2*Lr)
		turtle.penup()
		for j in range(1,3):
			turtle.left(90)
			turtle.forward(j*Lr)
		turtle.right(90)
		turtle.pendown()

inp = open('input.txt', 'r')
s = inp.readlines()


for stroka in s:
	for slovo in stroka.split():
		for cif in bin(int(slovo))[2:]:
			Chislo(int(cif))
		turtle.penup()
		turtle.forward(Lr*3)
		turtle.pendown()	
	turtle.penup()
	turtle.goto(0, turtle.ycor()-(Lr*3))
	turtle.pendown()

inp.close()
turtle.done()