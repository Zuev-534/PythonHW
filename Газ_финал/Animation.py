from random import randint
import turtle
import numpy as np


turtle.speed(100)
site_of_box = 500
turtle.penup()
turtle.goto(-site_of_box/2, site_of_box/2)
turtle.pendown()
for i in range(4):
	turtle.forward(site_of_box)
	turtle.right(90)
turtle.penup()
number_of_turtles = 20
Time_lim = 10000
Position = [(0.0, 0.0)]*number_of_turtles
N=2

dt = 1

pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]



for time in range(0, Time_lim, dt):
	input = open((str(time) + '.txt'), 'r')
	for i in range(number_of_turtles):
		for unit in pool:
			unit.penup()
			unit.speed(1000)
		x, y = (input.readline()).split()
		pool[i].goto(float(x),float(y))
	input.close()

