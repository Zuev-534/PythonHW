import math
import pygame
from pygame.draw import *
from random import randint

W = 800
FPS = 60
num_of_balls = 4
num_of_squares = 3
site_of_square = 50

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def ball_draw(scrn, bll):
    """
    Функция отрисовки нашего объекта
    :param bll: принимает значение массива с данными в порядке (радиус, абсцисса центра, ордината центра,
     абсц_скорость, орд_скорость, цвет)
    :param scrn: поверхность для отрисовки
    :return: ---
    """
    circle(scrn, bll[5], (bll[1], bll[2]), bll[0])


def square_draw(scrn, squar):
    """
    Функция отрисовки специального объекта
    :param squar: принимает значение массива с данными в порядке (сторона, абсцисса центра, ордината центра,
     абсц_скорость, орд_скорость, цвет)
    :param scrn: поверхность для отрисовки
    :return: ---
    """
    rect(scrn, squar[5], ((squar[1] - int(squar[0] / 2), squar[2] - int(squar[0] / 2)), (squar[0], squar[0])))


def moved(unt):
    """
    Функция, изменяющая координаты
    :param unt: объект, который мы двигаем
    :return: объект после передвижения
    """
    for i in (1, 2):
        if (unt[i] >= W - unt[0]) or (unt[i] <= unt[0]):
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


def gui(scrn, scr, num, spc_num, countdown, size_of_molodec):
    """
    Отрисовка пользовательского интерфейса
    :param scrn: поверхность для вывода
    :param scr: счет пользователя
    :param num: количество шаров
    :param spc_num: количество спецобъектов
    :param countdown: количество секунд после победы
    :param size_of_molodec: размерный коэффициент поздравления(1 - весь экран)
    :return: размерный коэффициент поздравления(1 - весь экран)
    """
    score_draw(scrn, scr)
    if scr >= num + spc_num*10:
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


def render_ball(scrn, obj):
    """
    Функция, отрисовки и просчета координат
    :param scrn: поверхность для отрисовки
    :param obj: объект, который нужно передвинуть и отрисовать
    :return: объект с измененными координатами
    """
    for unit in obj:
        unit = moved(unit)
        if unit[0] > 0:
            ball_draw(scrn, unit)
    return obj


def render_square(scrn, squar):
    """
    Функция, отрисовки и просчета координат
    :param scrn: поверхность для отрисовки
    :param squar: специальный объект, который нужно передвинуть и отрисовать
    :return: объект с измененными координатами
    """
    for unit in squar:
        unit = moved(unit)
        if unit[0] > 0:
            square_draw(scrn, unit)
    return squar


def kill(evnt, obj, squar, scr):
    """
    Функция "убийства" шариков
    :param evnt: событие
    :param obj: массив объектов
    :param squar: массив специальных объектов
    :param scr: счёт
    :return: кортеж (массив, счёт)
    """
    xb, yb = evnt.pos
    for unit in obj:
        if (unit[1] - xb) ** 2 + (unit[2] - yb) ** 2 <= unit[0] ** 2:
            if unit[0] > 0:
                scr += 1
            unit[0] = 0
    for unit in squar:
        if (abs(unit[1] - xb) <= unit[0] / 2) and (abs(unit[2] - yb) <= unit[0] / 2):
            if unit[0] > 0:
                scr += 10
            unit[0] = 0
    return obj, squar, scr


def event_processing(evnt, obj, squar, scr):
    """
    Обработка поступающих событий
    :param evnt: список событий
    :param obj: массив объектов
    :param squar: массив специальных объектов
    :param scr: счёт
    :return: кортеж (окончание игры, массив объектов, счёт)
    """
    for event in evnt:
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            obj, squar, scr = kill(event, obj, squar, scr)
    return False, obj, squar, scr


def gui_end(scrn, point_x, point_y):
    """
    Функция, выводящая просьбу о вводе имени
    :param scrn: поверхность для вывода
    :param point_x: абцисса отрисовки поверхности(левый верхний угол)
    :param point_y: ордината отрисовки поверхности(левый верхний угол)
    :return: ---
    """
    pygame.display.set_caption('Congratulations!!')
    endtext_font = pygame.font.SysFont("", 45)
    endtext_texture = endtext_font.render('Введите своё имя и нажмите SPACE:', False, GREEN)
    scrn.blit(endtext_texture, (point_x, point_y))
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
    """
    Функция, считывающая нажатые клавиши(и некоторые сочеттания). Работает до встречи с пробелом
    :return: сторку, с нажатыми клавишами(и некоторые сочеттания) как символами юникода
    """
    screen = pygame.display.set_mode((W, W))
    pygame.display.update()
    clock = pygame.time.Clock()
    nick = ''
    finished = False
    ended = False
    while not (finished or ended):
        clock.tick(FPS)
        screen.fill(BLACK)
        gui_end(screen, (W / 4), W / 3)
        finished, nick, ended = char_input(pygame.event.get(), nick)
        text_render(screen, nick, W / 4 + 10, W / 3 + 50)
        pygame.display.update()
    return nick


def text_render(scrn, nm, point_x, point_y):
    """
    Функция, отрисовывающая текст
    :param scrn: поверхность для вывода
    :param nm: текст для вывода
    :param point_x: абсцисса левой верхней точки поверхности
    :param point_y: ордината левой верхней точки поверхности
    :return: ---
    """
    realtime_name_font = pygame.font.SysFont("", 30)
    realtime_name_texture = realtime_name_font.render(nm, False, GREEN)
    scrn.blit(realtime_name_texture, (point_x, point_y))


def render_table(tab):
    """
    Функция, рисующая таблицу после записи в файл
    :param tab: итоговая таблица
    :return: "Правда". Просто для обрыва цикла и корректного завершения программы
    """
    pygame.display.set_caption('Champions')
    screen = pygame.display.set_mode((W, W))
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        screen.fill(BLACK)
        i = 0
        text_render(screen, "ТАБЛИЦА ЛИДЕРОВ", W / 3, 20)
        for zeile in tab:
            i = i + 1
            stroka = zeile[0][0:8] + " " + zeile[1][0:8]
            text_render(screen, stroka, 30, 20 + i * 40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.update()
                return True
        pygame.display.update()


def champ_table(tab, tuzu):
    """
    Функция, вносящая новый рекорд при его появлении
    :param tab: таблица чемпионов (массив пар "имя" и "счет")
    :param tuzu: новый результат (пара "имя" и "счёт")
    :return: измененная таблица
    """
    for i in range(len(tab)):
        if tab[i][1] == tuzu[1]:
            tab[i][0] = tuzu[0]
        if float(tab[i][1]) > float(tuzu[1]):
            temp = tab[i]
            tab[i] = tuzu
            tuzu = temp
    return tab


def igra(finished=False, player_won=False, player_won_count=0, timer=2,
         score=0, cong_size=0.1):
    """
    Функция, запускающая экран с игрой на время
    :param finished: условие завершения
    :param player_won: условие завершения
    :param player_won_count: счетчик кадров после победы
    :param timer: время задержки на поздравлении после победы(секунды)
    :param score: счет игрока
    :param cong_size: размер текста-поздравления
    :return: количество кадров, затраченных на "уничтожение" шариков
    """
    f_number = 0
    ball = [[randint(30, 50), randint(100, W - 100), randint(100, W - 100), randint(-7, 7), randint(-7, 7),
             COLORS[randint(0, 5)]] for _ in range(num_of_balls)]
    square = [[site_of_square, randint(100, W - 100), randint(100, W - 100), randint(-7, 7), randint(-7, 7),
               COLORS[randint(0, 5)]] for _ in range(num_of_squares)]

    pygame.display.set_caption('KILL THEM ALL')
    pygame.event.set_grab(True)
    screen = pygame.display.set_mode((W, W))
    pygame.display.update()
    clock = pygame.time.Clock()
    while not (finished or player_won):
        clock.tick(FPS)
        screen.fill(BLACK)

        finished, ball, square, score = event_processing(pygame.event.get(), ball, square, score)
        ball = render_ball(screen, ball)
        square = render_square(screen, square)

        cong_size, player_won_count = gui(screen, score, num_of_balls, num_of_squares, player_won_count, cong_size)

        if player_won_count >= timer:
            player_won = True
        pygame.display.update()
        f_number += 1
    return f_number


# Начало игры
pygame.init()

F = igra()
# Конец игры

# Ввод имени
# Без проверки на дурака
Nickname = name_input()

# Считывание таблицы
table = []
with open('Top10.txt', 'r') as T:
    for line in T:
        table.append(line.split())

# Изменение таблицы лидеров
table = champ_table(table, [Nickname[0:8], str(int(F / num_of_balls))[0:8]])

# Запись актуальной таблицы лидеров
with open('Top10.txt', 'w') as T:
    for line in table:
        T.write(line[0] + " " + line[1] + "\n")

# Отрисовка таблицы лидеров
render_table(table)

pygame.display.update()
pygame.quit()
