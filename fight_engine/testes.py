import pygame as pg
import os
import sys
from settings import *


pg.init()

Tela = pg.display.set_mode()
fonte = pg.font.SysFont('arial', 19, True, False)
Relogio = pg.time.Clock()   

Diretorio = os.path.dirname(__file__)
Imagens = os.path.join(Diretorio, 'imagens')
sfc = pg.image.load(os.path.join(Imagens, 'ryu.png'))     


golpe = ((170,460), (110,95))
        
continuar = True         
while continuar:
    for evento in pg.event.get():
            if evento.type == pg.KEYDOWN:
                if evento.type == pg.QUIT or evento.key == pg.K_ESCAPE:
                    continuar = False
                    pg.quit()
                    sys.exit()

    Tela.fill((255,255,255))
# TESTES
    r1 = pg.Rect((100,100), (150, 150))
    
    pg.draw.rect(Tela, 'Red', r1, 3)

    r2 = pg.Rect((300,300), (300, 300))
    r2.bottom = r1.bottom
    r2.centerx = r1.centerx
    
    # r2.centerx = r2.centerx - 50

    pg.draw.rect(Tela, 'Blue', r2, 3)    
    
    Tela.blit(pg.transform.scale(sfc, (r2.width, r2.height)), (r2.x, r2.y))
    
# FIM TESTES    
    Relogio.tick(FPS)
    pg.display.flip()

    
