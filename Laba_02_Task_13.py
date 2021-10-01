import turtle

# Изначальный "краденный" смайл был немного изменен
# https://www.geeksforgeeks.org/draw-smiling-face-emoji-using-turtle-in-python/

turtle.shape('turtle')
turtle.speed(100)

def glaz(col, rad):
	turtle.pendown()
	turtle.fillcolor(col)
	turtle.begin_fill()
	turtle.circle(rad)
	turtle.end_fill()
	turtle.penup()


turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.penup()

turtle.goto(-40, 120)
glaz('white', 15)
turtle.goto(40, 120)
glaz('white', 15)

turtle.goto(0, 100)
turtle.pendown()
turtle.setheading(90)
turtle.width(5)
turtle.forward(10)
turtle.penup()

turtle.setheading(0)
turtle.goto(-40, 85)
turtle.pendown()
turtle.width(5)
turtle.right(90)
turtle.circle(40, 180)


turtle.done()