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
sfc = pg.image.load(os.path.join(Imagens, 'basico.png'))
tatame = pg.image.load(os.path.join(Imagens, 'tatame.png'))     

superficie = pg.Surface(TELA_RESOLUCAO)

ve1 = 100, 400
ve1 = 100, 400
ve2 = 200, 200
vd3 = 300, 200
vd4 = 400, 400


def Poligono(indice):
    # ve1 += ve1
    # ve2 += ve2
    # vd3 += vd3
    # vd4 += vd4
    pg.draw.polygon(Tela, 'Green', (ve1, ve2, vd3, vd4))

continuar = True         
while continuar:
    for evento in pg.event.get():
            if evento.type == pg.KEYDOWN:
                if evento.type == pg.QUIT or evento.key == pg.K_ESCAPE:
                    continuar = False
                    pg.quit()
                    sys.exit()

    Tela.fill((255,255,255))

    for i in range(3):
        Poligono(i)

# TESTES
    
    # r2.centerx = r2.centerx - 50
    # superficie.fill(ROSA)
    # sfc.convert(superficie)
    # Tela.blit(pg.transform.scale(sfc, (r2.width, r2.height)), (r2.x, r2.y))
    
# FIM TESTES    
    Relogio.tick(FPS)
    pg.display.flip()

    
