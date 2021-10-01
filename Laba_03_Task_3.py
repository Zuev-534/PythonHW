from random import randint
import turtle


number_of_turtles = 20
steps_of_time_number = 100000

# Такое изменение pool увидел у соседа и оно мне понравилось
cheperaha = [turtle.Turtle(shape='circle'), 0, 0, 3, 60, 0, -10]
# obj, x, y, vx, vy, ax, ay
dt = 0.1

for i in range(steps_of_time_number):
	for j in (1, 2):
		cheperaha[j] += cheperaha[j+2]*dt + cheperaha[j+4]*0.5*dt**2
		cheperaha[j+2] += cheperaha[j+4]*dt
	cheperaha[0].goto(cheperaha[1], cheperaha[2])
	if cheperaha[2] <= 0:
		cheperaha[4] *= -0.9
		cheperaha[2] = 3