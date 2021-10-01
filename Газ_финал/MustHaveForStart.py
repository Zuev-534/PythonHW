from random import randint
import turtle
import numpy as np

turtle.shape('circle')
turtle.speed(100)
turtle.penup()

number_of_turtles = 50
site_of_box = 500
particles_on_site = 10

Particles_position = [(randint(-site_of_box/2, site_of_box/2), randint(-site_of_box/2, site_of_box/2)) for i in range(number_of_turtles)]
Board_particles_position = [0, 0]*(particles_on_site*4)
Velocity = [0, 0]*number_of_turtles


def Doc_BP():
	turtle.goto(-site_of_box/2, site_of_box/2)
	for i in range(0, particles_on_site*4, particles_on_site):
		for j in range(particles_on_site):
			turtle.forward(site_of_box/particles_on_site)
			Board_particles_position[i + j] = turtle.pos()
		turtle.right(90)

# for i in range(number_of_turtles):
# 	turtle.pencolor("blue")
# 	turtle.goto(Particles_position[i][0], Particles_position[i][1])
# 	turtle.stamp()

# for i in range(particles_on_site*4):
# 	turtle.pencolor("black")
# 	turtle.goto(Board_particles_position[i][0], Board_particles_position[i][1])
# 	turtle.stamp()