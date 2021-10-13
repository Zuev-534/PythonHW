import os
import sys
import math
import pygame
from pygame.draw import *
from random import randint

FPS = 10
W = 800

num_of_balls = 6
score = 0
cong_size = 0.1

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

ball = [[randint(30, 50), randint(100, W - 100), randint(100, W - 100), randint(-7, 7), randint(-7, 7),
         COLORS[randint(0, 5)]] for i in range(num_of_balls)]
# [r, x, y, vx, vy, color]


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
    for i in (1, 2):
        if ((unt[i] >= W - unt[0]) or (unt[i] <= unt[0])):
            unt[i + 2] = unt[i + 2] * (-1)
            unt[i] = unt[i] + unt[i + 2]
        unt[i] += unt[i + 2]
    return unt


def score_draw(scrn, scr, point=(0, 0)):
    """
    Функция, выводящая счет
    :param scrn: поверхность для вывода
    :param scr: счет пользователя
    :param point: место отрисовки поверхности(левый верхний угол)
    :return: ---
    """
    score_font = pygame.font.SysFont("", 45)
    score_texture = score_font.render(('Счёт: ' + str(scr)), False, (120, 128, 255))
    scrn.blit(score_texture, point)


def cong_draw(scrn, size_of_molodec):
    """
    Функция, поздравляющая пользователя
    :param scrn: поверхность для вывода
    :param size_of_molodec: размерный коэффициент поздравления(1 - весь экран)
    :return: ---
    """
    cong_font = pygame.font.SysFont("", int(100 * abs(math.sin(1.6 * size_of_molodec))))
    cong_texture = cong_font.render('YOU ARE MOLODEC!!!', False, (255, 255, 0))
    scrn.blit(cong_texture, (((1 - abs(math.sin(1.6 * size_of_molodec))) * W) / 2, W / 2))


def gui(scrn, scr, num, size_of_molodec=1):
    """
    Отрисовка пользовательского интерфейса
    :param scrn: поверхность для вывода
    :param scr: счет пользователя
    :param num: количество шаров
    :param size_of_molodec: размерный коэффициент поздравления(1 - весь экран)
    :return: размерный коэффициент поздравления(1 - весь экран)
    """
    score_draw(scrn, scr)
    if scr >= num:
        return endgame(scrn, scr, size_of_molodec)
    else:
        return 0


def endgame(scrn, scr, size_of_molodec):
    """
    Функция отрисовывает поздравления и список лидеров(второе только планируется)
    :param scrn: поверхность для вывода
    :param scr: счет пользователя
    :param size_of_molodec: размерный коэффициент поздравления(1 - весь экран)
    :return: размерный коэффициент поздравления(1 - весь экран)
    """
    scrn.fill(BLACK)
    score_draw(scrn, scr, (W / 2 - W / 17, W / 4))
    cong_draw(scrn, size_of_molodec)
    size_of_molodec = size_of_molodec + (1 / FPS)
    return size_of_molodec


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

def event_processing(evnt, obj, scr):
    """
    Обработка поступающих событий
    :param evnt: список событий
    :param obj: массив объектов
    :param scr: счёт
    :return: кортеж (окончание игры, массив объектов, счёт)
    """
    for event in evnt:
        if event.type == pygame.QUIT:
            return True, obj, scr
        elif event.type == pygame.MOUSEBUTTONDOWN:
            obj, scr = kill(event, obj, scr)
    return False, obj, scr





pygame.init()
pygame.event.set_grab(True)
screen = pygame.display.set_mode((W, W))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    screen.fill(BLACK)

    finished, ball, score = event_processing(pygame.event.get(), ball, score)

    ball = render(screen, ball)
    cong_size = gui(screen, score, num_of_balls, cong_size)

    pygame.display.update()
pygame.quit()
