import pygame
from pygame.draw import *

pygame.init()

FPS = 30
R = [10, 10, 100, 100]
screen = pygame.display.set_mode((794, 1123))
bg = pygame.image.load('17_1.png')
bg_place = (0, 0, 794, 1123)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
def El(cv, A):
    ellipse(screen, cv, A) 

while not finished:
    clock.tick(FPS)
    screen.fill('white')
    screen.blit(bg, bg_place)
    for i in pygame.event.get():
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_s:
                R[3] += 30
            elif i.key == pygame.K_w:
                R[3] -= 30
            elif i.key == pygame.K_d:
                R[2] += 30
            elif i.key == pygame.K_a:
                R[2] -= 30
            elif i.key == pygame.K_UP:
                R[1] -= 30
            elif i.key == pygame.K_RIGHT:
                R[0] += 30
            elif i.key == pygame.K_LEFT:
                R[0] -= 30
            elif i.key == pygame.K_DOWN:
                R[1] += 30
            if i.key == pygame.K_g:
                R[3] += 3
            elif i.key == pygame.K_t:
                R[3] -= 3
            elif i.key == pygame.K_h:
                R[2] += 3
            elif i.key == pygame.K_f:
                R[2] -= 3
            elif i.key == pygame.K_i:
                R[1] -= 3
            elif i.key == pygame.K_l:
                R[0] += 3
            elif i.key == pygame.K_j:
                R[0] -= 3
            elif i.key == pygame.K_k:
                R[1] += 3
            elif i.key == pygame.K_e:
                print(R)
    El('cyan', R)
    pygame.display.update()
pygame.quit()