import math
import pygame
from pygame.draw import *
from random import randint

W = 800
FPS = 24
num_of_balls = 6

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
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


def gui(scrn, scr, num, countdown, size_of_molodec):
    """
    Отрисовка пользовательского интерфейса
    :param scrn: поверхность для вывода
    :param scr: счет пользователя
    :param num: количество шаров
    :param countdown: количество секунд после победы
    :param size_of_molodec: размерный коэффициент поздравления(1 - весь экран)
    :return: размерный коэффициент поздравления(1 - весь экран)
    """
    score_draw(scrn, scr)
    if scr >= num:
        return endgame(scrn, scr, size_of_molodec), (countdown + 1 / FPS)
    else:
        return 0, 0


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
    :param obj: объект, который нужно передвинуть и отрисовать
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
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            obj, scr = kill(event, obj, scr)
    return False, obj, scr


def gui_end(scrn, point_x, point_y):
    """
    Функция, выводящая просьбу о вводе имени
    :param scrn: поверхность для вывода
    :param point: место отрисовки поверхности(левый верхний угол)
    :return: ---
    """
    pygame.display.set_caption('Congratulations!!')
    Endtext_font = pygame.font.SysFont("", 45)
    Endtext_texture = Endtext_font.render(('Введите своё имя и нажмите SPACE:'), False, GREEN)
    scrn.blit(Endtext_texture, (point_x, point_y))
    rect(scrn, GREEN, ((point_x, point_y + 30), (300, 50)), 3)


def char_input(evnt, nm):
    for event in evnt:
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            nm = ((nm[::-1])[1:])[::-1]
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            return False, nm, True
        elif event.type == pygame.KEYDOWN:
            nm += str(event.unicode)
    return False, nm, False


def name_input():
    screen = pygame.display.set_mode((W, W))
    pygame.display.update()
    clock = pygame.time.Clock()
    Name = ''
    finished = False
    ended = False
    while not (finished or ended):
        clock.tick(FPS)
        screen.fill(BLACK)
        gui_end(screen, (W / 4), W / 3)
        finished, Name, ended = char_input(pygame.event.get(), Name)
        text_render(screen, (Name), W / 4 + 10, W / 3 + 50)

        pygame.display.update()
    return Name


def text_render(scrn, nm, point_x, point_y):
    realtimeNM_font = pygame.font.SysFont("", 30)
    realtimeNM_texture = realtimeNM_font.render((nm), False, GREEN)
    scrn.blit(realtimeNM_texture, (point_x, point_y))


def render_table(tab):
    pygame.init()
    pygame.display.set_caption('Champions')
    screen = pygame.display.set_mode((W, W))
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        screen.fill(BLACK)
        i = 0
        text_render(screen, "ТАБЛИЦА ЛИДЕРОВ", W/3, 20)
        for line in tab:
            i = i + 1
            stroka = line[0][0:8] + " " + line[1][0:8]
            text_render(screen, stroka, 30, 20 + i * 40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.update()
                pygame.quit()
        pygame.display.update()


def Champ_table(tab, line):
    temp = [[], []]
    for player in tab:
        if player[1] == line[1]:
            player[0] = line[0] + "and other"
        if float(player[1]) > float(line[1]):
            temp = player
            player = line
            line = temp
    render_table(tab)
    print(tab)
    return tab


def igra(finished=False, player_won=False, player_won_count=0, timer=2,
         score=0, cong_size=0.1):
    F_number = 0
    ball = [[randint(30, 50), randint(100, W - 100), randint(100, W - 100), randint(-7, 7), randint(-7, 7),
             COLORS[randint(0, 5)]] for i in range(num_of_balls)]
    pygame.display.set_caption('KILL THEM ALL')
    pygame.event.set_grab(True)
    screen = pygame.display.set_mode((W, W))
    pygame.display.update()
    clock = pygame.time.Clock()
    while not (finished or player_won):
        clock.tick(FPS)
        screen.fill(BLACK)

        finished, ball, score = event_processing(pygame.event.get(), ball, score)
        ball = render(screen, ball)

        cong_size, player_won_count = gui(screen, score, num_of_balls, player_won_count, cong_size)

        if player_won_count >= timer:
            player_won = True
        pygame.display.update()
        F_number += 1
    return F_number


pygame.init()

F = igra()

# Без проверки на дурака
Nickname = name_input()
table = []
with open('Top10.txt', 'r') as T:
    for line in T:
        table.append(line.split())

table = Champ_table(table, [Nickname[0:8], str(F / num_of_balls)[0:8]])
print(table)
print(str(F / num_of_balls)[0:8])

with open('Top10.txt', 'w') as T:
    for line in table:
        T.write(line[0] + " " + line[1] + "\n")

print(table)

pygame.display.update()
pygame.quit()
