import turtle

turtle.shape('turtle')
turtle.speed(100)

turtle.forward(5)
turtle.left(90)

for x in range(1, 360):
	turtle.left(4)
	turtle.forward(x/100)

turtle.done()