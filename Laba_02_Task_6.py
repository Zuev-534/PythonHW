import turtle

turtle.shape('turtle')
turtle.speed(5)

site = 10
step = 10

def Sharshi(s):
	for i in range(4):
		turtle.left(90)
		turtle.forward(s)
	turtle.right(45)
	turtle.penup()
	turtle.forward(step/2**0.5)
	turtle.pendown()
	turtle.right(-45)
while True:
	Sharshi(site)
	site += step

turtle.done()