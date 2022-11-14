import pygame as pg
from settings import *

mapa = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]

# self.P1.x = ((TELA_LARGURA // 4))
# self.P1.y = (TELA_ALTURA_CHAO - self.P1.h)
# self.P1.w = 80
# self.P1.h = 150                

ryu = [pg.Rect(((TELA_LARGURA // 4)), (TELA_ALTURA_CHAO - 150), 80, 150 ), "ryu.png"]