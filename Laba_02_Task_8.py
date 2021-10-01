import turtle

turtle.shape('turtle')
turtle.speed(100)

for x in range(10, 1000, 5):
	turtle.left(90)
	turtle.forward(x)

turtle.done()