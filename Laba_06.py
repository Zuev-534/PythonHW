import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 10
W = 800
screen = pygame.display.set_mode((W, W))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def ball_draw(scrn, ball):
    """
    Функция отрисовки нашего объекта
    :param ball: принимает значение массива с данными в порядке (радиус, абсцисса, ордината, абсц_скорость, орд_скорость, цвет)
    :param scrn: поверхность для отрисовки
    :return: ---
    """
    circle(scrn, ball[5], (ball[1], ball[2]), ball[0])

def moved(unt):
    """
    Функция, изменяющая координаты
    :param unt: объект, который мы двигаем
    :return: объект после передвижения
    """
    for i in (1,2):
        if ((unt[i] >= W - unt[0]) or (unt[i] <= unt[0])):
            unt[i + 2] = unt[i + 2] * (-1)
            unt[i] = unt[i] + unt[i + 2]
        unt[i] += unt[i + 2]
    return unt

def score_draw(scrn, scr):
    """
    Функция, выводящая счет
    :param scrn: поверхность для вывода
    :param scr: счет пользователя
    :return: ---
    """
    score_font = pygame.font.SysFont("", 45)
    score_texture = score_font.render(('Счёт: ' + str(scr)), False, (120, 128, 255))
    scrn.blit(score_texture, (0, 0))

def cong_draw(scrn):
    """
    Функция, поздравляющая пользователя
    :param scrn: поверхность для вывода
    :return: ---
    """
    cong_font = pygame.font.SysFont("", 100)
    cong_texture = cong_font.render('YOU ARE MOLODEC!!!', False, (255, 255, 0))
    screen.blit(cong_texture, (25, W / 2))

def gui(scrn, scr, num):
    """
    Отрисовка пользовательского интерфейса
    :param scrn: поверхность для вывода
    :param scr: счет пользователя
    :param num: количество шаров
    :return: ---
    """
    score_draw(screen, score)
    if score >= num_of_balls:
        cong_draw(screen)

def render(scrn, obj):
    """
    Функция, отрисовки и просчета координат
    :param scrn: поверхность для отрисовки
    :param obj: объект, который нуно передвинуть и отрисовать
    :return: объект с измененными координатами
    """
    for unit in obj:
        for i in (1, 2):
            unit = moved(unit)
        if unit[0] > 0:
            ball_draw(scrn, unit)
    return obj

def kill(evnt, obj, scr):
    """
    Функция "убийства" шариков
    :param evnt: событие
    :param obj: массив объектов
    :param scr: счёт
    :return: кортеж (массив, счёт)
    """
    xb, yb = evnt.pos
    for unit in obj:
        if ((unit[1] - xb) ** 2 + (unit[2] - yb) ** 2 <= unit[0] ** 2):
            if unit[0] > 0:
                scr += 1
            unit[0] = 0
    return (obj, scr)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

num_of_balls = 15
score = 0


ball = [[randint(30, 50), randint(100, W - 100), randint(100, W - 100), randint(-7, 7), randint(-7, 7),
         COLORS[randint(0, 5)]] for i in range(num_of_balls)]
# [r, x, y, vx, vy, color]


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ball, score = kill(event, ball, score)

    ball = render(screen, ball)
    gui(screen, score, num_of_balls)

    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
