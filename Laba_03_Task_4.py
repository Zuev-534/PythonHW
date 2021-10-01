from random import randint
import turtle

dt = 0.1
site = 500
number_of_turtles = 20
steps_of_time_number = 100000

# Такое изменение pool увидел у соседа и оно мне понравилось
pool = [[turtle.Turtle(shape='circle'), 0, 0, 0, 0, 0, 0] for i in range(number_of_turtles)]
# obj, x, y, vx, vy, ax, ay

for unit in pool:
	for i in (1,2):
		unit[i]   += randint(int(-site/2), int(site/2))
		unit[i+2] += randint(int(-site/8), int(site/8))
		unit[0].penup()
		unit[0].speed(100)

pool[0][0].goto(-site/2, site/2)
for i in range(4):
	pool[0][0].pendown()
	pool[0][0].forward(site)
	pool[0][0].right(90)
	pool[0][0].penup()

for i in range(steps_of_time_number):
	for unit in pool:
		for j in (1, 2):
			unit[j] += unit[j+2]*dt 
			unit[j+2] += unit[j+4]*dt 
			if abs(unit[j]) >= site/2:
				unit[j+2] *= -1
		unit[0].goto(unit[1], unit[2])