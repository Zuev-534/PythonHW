import turtle

turtle.shape('turtle')
turtle.speed(100)

R=100

turtle.left(90)
for i in range(10):
    turtle.circle(R+0.5*R*(i//2))
    turtle.left(180)   


turtle.done()