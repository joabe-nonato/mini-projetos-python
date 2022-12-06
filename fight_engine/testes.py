import pygame as pg
import os
import sys
from settings import *


larga = 900
altu = 600
pg.init()

Tela = pg.display.set_mode((larga, altu))
# fonte = pg.font.SysFont('arial', 19, True, False)
Relogio = pg.time.Clock()   

# Diretorio = os.path.dirname(__file__)
# Imagens = os.path.join(Diretorio, 'imagens')
# sfc = pg.image.load(os.path.join(Imagens, 'basico.png'))
# tatame = pg.image.load(os.path.join(Imagens, 'tatame.png'))     

superficie = pg.Surface((larga, altu))

cor_grama = [0, 202, 0]
cor_zebra = [0, 0, 0]
centrox = (Tela.get_width() / 2)

def desenhar(cor, ve1, ve2, vd3, vd4):
    pg.draw.polygon(Tela, cor, (ve1, ve2, vd3, vd4))

def Grama(i, r, y, h):        
    ve2 = 0, y
    ve1 = 0, y + h
    vd3 = larga, y
    vd4 = larga, y + h
    
    if r == 0:
        cor_grama = [0, 202, 0]
    else:
        cor_grama = [0, 111, 0]    

    desenhar(cor_grama, ve1, ve2, vd3, vd4)
    

def Zebra(i, r, y, h):        
    ve2 = (centrox + (i * 5)), y
    ve1 = (centrox + (i * 5)), y + h
    vd3 =  (centrox + (i * 10)) , y
    vd4 = (centrox + (i * 20)), y + h
    
    if r == 0:
        cor_zebra = [0, 0, 0]
    else:
        cor_zebra = [255, 255, 255]    

    desenhar(cor_zebra, ve1, ve2, vd3, vd4)

continuar = True         
while continuar:
    for evento in pg.event.get():
            if evento.type == pg.KEYDOWN:
                if evento.type == pg.QUIT or evento.key == pg.K_ESCAPE:
                    continuar = False
                    pg.quit()
                    sys.exit()

    Tela.fill((111,111,111))

    py = (Tela.get_height() / 2)
    ph = 1
    for i in range(20):
        resto = i % 2
        py += (2 * i)
        ph += (1 * i)
        Grama(i, resto, py, ph)
        Zebra(i, resto, py, ph)

# TESTES
    
    # r2.centerx = r2.centerx - 50
    # superficie.fill(ROSA)
    # sfc.convert(superficie)
    # Tela.blit(pg.transform.scale(sfc, (r2.width, r2.height)), (r2.x, r2.y))
    
# FIM TESTES    
    Relogio.tick(FPS)
    pg.display.flip()

    
