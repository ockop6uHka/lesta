import pygame as pg
import sys
from game_config import *
from board import *
pg.init()
clock = pg.time.Clock()
fil_board()
run = True
while run:  #логика главного цикла игры

    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            run= False
        
        elif event.type == pg.MOUSEBUTTONDOWN:
            btn_down( event.pos)
        elif event.type == pg.MOUSEBUTTONUP:
            btn_up( event.pos)

    if run != False:
        screen.blit(bg,(0,0))
        screen.blit(pg.image.load('images/sq_yel.png'), (17,75))
        screen.blit(pg.image.load('images/sq_ora.png'), (150,75))
        screen.blit(pg.image.load('images/sq_red.png'), (281,75))
        cells.draw(screen)
        balls.draw(screen)
        buttons.draw(screen)
        comb_check()
        pg.display.update()
       
            
