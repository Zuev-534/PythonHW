import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

# Глаза и зрачки
circle(screen, (255, 255, 0), (200, 175), 150)
circle(screen, (255, 0, 0), (130, 130), 20)
circle(screen, (255, 0, 0), (270, 130), 35)
circle(screen, (0, 0, 0), (130, 130), 7)
circle(screen, (0, 0, 0), (270, 130), 7)

#Зубы и брови
x1 = 140; y1 = 260
x2 = 260; y2 = 285
rect(screen, "white", (x1, y1, x2 - x1, y2 - y1))
line(screen, "black", (160, 120), (100, 90), 10)
line(screen, "black", (240, 100), (300, 70), 10)


# Штрихи из примера
N = 10
rect(screen, "black", (x1, y1, x2 - x1, y2 - y1), 4)
h = (x2 - x1) // (N + 1)
x = x1 + h
for i in range(N):
    line(screen, "black", (x, y1), (x, y2))
    x += h


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()