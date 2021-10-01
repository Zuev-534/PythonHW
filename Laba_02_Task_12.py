import turtle

turtle.shape('turtle')
turtle.speed(100)

R=100

turtle.left(90)
for i in range(1, 10):
    turtle.circle(R, 180)
    turtle.circle(R/10, 180)


turtle.done()