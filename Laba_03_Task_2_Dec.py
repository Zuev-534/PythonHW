import turtle
from Laba_02_coordinates import GLIF, ANGLE
turtle.shape('turtle')
turtle.speed(50)
L = 30
Lsite = L
Ldiag = L*2**0.5
Otstup = Lsite * (0.25 + 2)
Rast_Bukv = Lsite * 0.5
Rast_Slov = Rast_Bukv + 0.75*Lsite

def Chislo(n):
	Cif = GLIF[n]
	for i in range(9):
		if Cif[i]!=0:
			turtle.pendown()
		else:
			turtle.penup()
		if i==6 or i==8:
			turtle.forward(Ldiag)
		else:
			turtle.forward(Lsite)
		turtle.right(ANGLE[i])
	turtle.penup()	


inp = open('Lab_02_input.txt', 'r')
s = inp.readlines() 

turtle.left(90)
for stroka in s:
	dx = 0
	for slovo in stroka.split():
		for glif in slovo:
			Chislo(int(glif))
			dx += 1 + Rast_Bukv / Lsite
			for i in [Rast_Bukv, 2*Lsite]:
				turtle.right(90)
				turtle.forward(i) 
			turtle.left(180)
		turtle.right(90)
		turtle.forward(Rast_Slov)
		turtle.left(90)
		dx +=  Rast_Slov / Lsite
	turtle.left(90)
	turtle.forward(dx*Lsite)
	turtle.left(90)
	turtle.forward(Otstup)
	turtle.left(180)
	
inp.close()
turtle.done()