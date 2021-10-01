from random import *
import turtle

turtle.shape('turtle')
turtle.speed(100)

for i in range(1, 100):
	turtle.left(randint(0, 360))
	turtle.forward(randint(1, 70))

turtle.done()