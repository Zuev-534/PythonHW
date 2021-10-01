import turtle

turtle.shape('turtle')
turtle.speed(100)

a = 10
s = 10

while True:
	turtle.left(90)
	turtle.forward(a)
	a += s

turtle.done()