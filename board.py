import pygame as pg
from math import *
from game_config import *

pg.init()


class Ball(pg.sprite.Sprite): #классы активных объектов фишек, кнопок и полей, на которых располагаются фишки
    def __init__(self, x,y, filename, index:str):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.index = index

class Buttons (pg.sprite.Sprite):
    def __init__(self, x,y, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

class Cell(pg.sprite.Sprite):
    def __init__(self, x,y, filename, index:str):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.index = index

def fil_board():
    x=50
    y=220 
    
    for i in range(5):  #логика заполнения доски объектами и создание им индексов, ссылающихся на массив board
        for j in range(5):
            if board[i][j] != '*':
                cells.add(Cell(x,y,  'images/open.png',str(i)+str(j)) )
            if board[i][j] == 'o':
                balls.add(Ball(x,y,  'images/sq_ora.png',str(i)+str(j)))
            elif board[i][j] == 'r':
                balls.add(Ball(x,y,  'images/sq_red.png',str(i)+str(j)))
            elif board[i][j] == 'y':
                balls.add(Ball(x,y,  'images/sq_yel.png',str(i)+str(j)))
            elif board[i][j] == '*':
                cells.add(Ball(x,y,  'images/block.png','99'))
            x = x + 66 
        y = y + 66
        x = 50
    x=50
    y=220

buttons.add(Buttons(470,330,  'images/restart.png'))    

    
def get_cell(position: str):
    for cell in cells:
        if cell.rect.collidepoint(position): #получение координатов объекта, считывая позицию мыши

            return cell
    return None

def get_button(position: str):
    for button in buttons:
        if button.rect.collidepoint(position):
            return button
    return None

def btn_down(position: str):
    global fil_index
    global cell
    global ggbutton
    cell = get_cell(position)
    button=get_button(position)   #
    ggbutton=button
    
    fil_index = ''
    if cell != None and cell.index!='99':   #запоминание индекса объекта при нажатия мыши
        fil_index= cell.index

def btn_up(position: str): #логика смены блоков только на соседние пустые клетки при отпускании мыши
    global board
    global cell
    global ggbutton
    button=get_button(position)  
    cell = get_cell(position)
    if cell != None and fil_index!='' and cell.index!='99' and int(fil_index[0])-int(cell.index[0])==0 and abs(int(fil_index[1])-int(cell.index[1]))==1:
        vertical = True
    else:
        vertical = False
    if cell != None and fil_index!='' and cell.index!='99' and abs(int(fil_index[0])-int(cell.index[0]))==1 and int(fil_index[1])-int(cell.index[1])==0:
        gorizontal = True
    else:
        gorizontal=False

    if cell != None and fil_index!='' and cell.index!='99' and vertical == True and gorizontal==False and board[int(cell.index[0])][int(cell.index[1])] == '0':
            board[int(fil_index[0])][int(fil_index[1])], board[int(cell.index[0])][int(cell.index[1])]= board[int(cell.index[0])][int(cell.index[1])], board[int(fil_index[0])][int(fil_index[1])]
            
            balls.empty()
            fil_board()
            pg.display.update()
            
    elif cell != None and fil_index!='' and cell.index!='99' and gorizontal==True and vertical==False and board[int(cell.index[0])][int(cell.index[1])] == '0':           
        board[int(fil_index[0])][int(fil_index[1])], board[int(cell.index[0])][int(cell.index[1])]= board[int(cell.index[0])][int(cell.index[1])], board[int(fil_index[0])][int(fil_index[1])]
        s_del = 0          
        balls.empty()
        fil_board()  #перерисовка новой позиции на доске
        pg.display.update()
            
    elif ggbutton!=None and button != None: 
        balls.empty()       
        board = [
    ['o','*','y','*','o'],  #логика кнопки рестарт
    ['r','0','y','0','o'],
    ['y','*','r','*','r'],
    ['o','0','o','0','y'],
    ['r','*','r','*','y'],]
        fil_board()
        pg.display.update()


def comb_check():    #логика завершения игры
    amount_o = 0
    amount_y = 0
    amount_r = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'y' and j==0:
                amount_y += 1
            elif board[i][j] == 'o' and j==2:
                amount_o += 1
            elif board[i][j] == 'r' and j==4:
                amount_r += 1
    if amount_o ==5 and amount_r ==5 and amount_y == 5:
        screen.blit(bg,(0,0))
        screen.blit(gg,(150,125))
        buttons.draw(screen)
        
pg.display.update()
