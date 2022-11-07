import pygame as pg
from game_config import *

pg.init()

WIDTH = 800
HEIGHT = 650
FPS = 30
WINDOW_SIZE = (600, 580)
BACKGROUND = (100,60,20)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY =(180,180,180)
SUPER_GREY = (90,90,90)
YELLOW =(255,255,0)
Orange=(240,142,45)
RED = (206,34,37)
Turquoise = (0,120,120)
Green = (44,181,44)
amount_o = 0
amount_y = 0
amount_r = 0

board = [
    ['o','*','y','*','o'],
    ['r','0','y','0','o'],
    ['y','*','r','*','r'],
    ['o','0','o','0','y'],
    ['r','*','r','*','y'],
]

fil_index = ''
screen = pg.display.set_mode(WINDOW_SIZE)
balls = pg.sprite.Group()   #создание группы спрайтов (активных объектов)
cells = pg.sprite.Group()
buttons = pg.sprite.Group()
bg = pg.image.load('images/fon.jpg').convert()
gg = pg.image.load('images/gg.jpg').convert()
