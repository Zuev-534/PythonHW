from random import randint
# import turtle
import numpy as np

# turtle.shape('circle')
# turtle.speed(100)
# turtle.penup()

number_of_turtles = 20
site_of_box = 500

Position = [(float(randint(-site_of_box/2, site_of_box/2)), float(randint(-site_of_box/2, site_of_box/2))) for i in range(number_of_turtles)]

Time_lim = 1000
dt = 0.1
N = 2
F_convergence = 10**6
F_distancing = 10**6
Velocity = [(float(randint(0, 2)), float(randint(0, 2))) for i in range(number_of_turtles)]
Acceleration = [(0.0, 0.0)]*number_of_turtles

# def Position_calc():


def Position_output(time):
	out = open((str(time) + '.txt'), 'w')
	for i in range(number_of_turtles):
		stroka = ''
		for dim in range(N):
			stroka = stroka + str(Position[i][dim]) + ' '
		out.write(stroka)
		if i < (number_of_turtles -1):
			out.write('\n')
	out.close()

for t in range(Time_lim):
	# Position_calc()
	for i in range(number_of_turtles):
		Position[i] = [(Position[i][dim] + dt*Velocity[i][dim] + dt**2*0.5*Acceleration[i][dim]) for dim in range(N)]
	Position_output(t)
	# Acceleration_calc()
	Acceleration = [(0, 0)]*number_of_turtles
	for i in range(number_of_turtles):
			Relative_position = Position
			for j in (k for k in range(number_of_turtles) if not(k == i)):
				D = [(Relative_position[j][dim] - Position[i][dim]) for dim in range(N)]
				R = 0
				for dim in range(N):
					R = R + (D[dim])**2
				r = R**0.5
				Force = -F_distancing/r**11 + F_convergence/r**5
				F = [(Force*D[dim]/r) for dim in range(N)]
				Acceleration[i] = [(Acceleration[i][dim]+ F[dim]) for dim in range(N)]
	# Velocity_calc()
	for i in range(number_of_turtles):
		Velocity[i] = [Velocity[i][dim] + dt*Acceleration[i][dim] for dim in range(N)]
		for dim in range(N):
			if abs(Position[i][dim]) > (site_of_box/2):
				Velocity[i][dim] = (-1)*Velocity[i][dim]
				for i in range(number_of_turtles):
					Position[i] = [(Position[i][dim] + 2*dt*Velocity[i][dim] + 2*dt**2*0.5*Acceleration[i][dim]) for dim in range(N)]
				Position_output(t)






















# 	for i in range(number_of_turtles):
# 		Position[i] = [(Position[i][dim] + dt*Velocity[i][dim] + dt**2*0.5*Acceleration[i][dim]) for dim in range(N)]



# def Acceleration_calc():
# 	for i in range(number_of_turtles):
# 		Relative_position = Position
# 		for j in (k for k in range(number_of_turtles) if not(k == i)):
# 			D = [(Relative_position[j][dim] - Position[i][dim]) for dim in range(N)]
# 			R = 0
# 			for dim in range(N):
# 				R = R + (D[dim])**2
# 			r = R**0.5
# 			# Force = -F_distancing/r**5 + F_convergence/r**2
# 			Force = F_convergence*r
# 			F = [(Force*D[dim]/r) for dim in range(N)]
# 			Acceleration[i] = [(Acceleration[i][dim]+ F[dim]) for dim in range(N)]
# 			print(Acceleration)


# def Velocity_calc():
# 	for i in range(number_of_turtles):
# 		Velocity[i] = [(Velocity[i][dim] + dt*Acceleration[i][dim]) for dim in range(N)]
# 		for dim in range(N):
# 			if abs(Position[i][dim]) > (site_of_box/2):
# 				Velocity[i] = (-1)*Velocity[i]