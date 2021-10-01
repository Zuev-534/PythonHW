import turtle

turtle.shape('turtle')
turtle.speed(100)

A = [1, 2, 2, 0, 0]
L=100

for a in A:
	turtle.left(90*(a-1))
	turtle.forward(L)

turtle.done()