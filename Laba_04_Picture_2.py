#Про прозрачный фон узнал на https://stackoverflow.com/questions/328061/how-to-make-a-surface-with-a-transparent-background-in-pygame
import pygame
from pygame.draw import *
from Laba_04_BD_Pic_CW import Alien
from Laba_04_BD_Pic_CW import Ufo
from Laba_04_BD_Pic_CW import Clouds

pygame.init()
Width, Height = 600, 800
screen = pygame.display.set_mode((Width, Height))
clock = pygame.time.Clock()
finished = False

S = [367, 543, 373, 600, 794, 562]
k_x = Width / 794
k_y = Height / 1123 
k = (k_x**2 + k_y**2)**0.5
FPS = 30
# Background
rect(screen, (0, 34, 43), (0, 0, Width, Height/2))
rect(screen, (34, 43, 0), (0, Height/2, Width, Height/2))
ellipse(screen, (242, 242, 242), (382 * k_x, 124 * k_y, 250*k, 250*k))
# Clouds
PlcC = pygame.Surface((S[4], S[5]), pygame.SRCALPHA, 32)
Clouds(PlcC)
screen.blit(pygame.transform.scale(PlcC, (int(k_x*S[4]), int(k_y*S[5]))), (0, 0))

# Alien
def Draw_Alien(screen_UN, X, Y, k_Alien_UN):
	PlcA = pygame.Surface((S[0], S[1]), pygame.SRCALPHA, 32)
	Alien(PlcA, 0, 0)
	screen_UN.blit(pygame.transform.scale(PlcA, (int(k_Alien_UN*S[0]), int(k_Alien_UN*S[1]))), (X, Y))

#UFO
def Draw_UFO(screen_UN, X, Y, k_Ufo_UN):
	PlcU = pygame.Surface((S[2], S[3]), pygame.SRCALPHA, 32)
	Ufo(PlcU, 0, 0)
	screen_UN.blit(pygame.transform.scale(PlcU, (int(k_Ufo_UN*S[2]), int(k_Ufo_UN*S[3]))), (X, Y))



# Positioning
k_Ufo = 0.8
k_Alien = 0.8
x_ufo, y_ufo = Width * 0.05 , Height * 0.4
x_alien, y_alien = Width * 0.5, Height * 0.6
# Execution
Draw_UFO(screen, x_ufo, y_ufo, k_Ufo)
Draw_Alien(screen, x_alien, y_alien, k_Alien)



pygame.display.update()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()