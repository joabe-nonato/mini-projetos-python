import pygame as pg
from settings import *
from objeto import *

cor = 'Blue'

class Player:
    def __init__(self, game) -> None:
        self.game = game
        self.x = 50
        self.y = 50
        self.obj = Objeto()        

    def movimento(self):
        global dx, dy, cor        
        dx = self.x
        dy = self.y

        if pg.KEYDOWN:           

            def colisao(plx):
                colide = False
                
                for o in self.game.objetos:                    
                    colide = pg.Rect.colliderect(plx, pg.Rect(o[0], o[1], BLOCO_LARGURA, BLOCO_ALTURA))
                    if colide:
                        break
                
                return colide

            keys = pg.key.get_pressed()           
            
        # UP | SOBE
            if keys[pg.K_w] and self.y > 0:
                # COLISÃO
                colide = colisao(pg.Rect(dx, dy - VELOCIDADE, PLAYER_LARGURA, PLAYER_ALTURA))
                if colide == False:
                    dy -= VELOCIDADE

        # DOWN | DESCE
            elif keys[pg.K_s] and self.y < ALTURA:
                # COLISÃO
                colide = colisao(pg.Rect(dx, dy + VELOCIDADE, PLAYER_LARGURA, PLAYER_ALTURA))
                if colide == False:
                    dy += VELOCIDADE
            
        # LEFT | ESQUERDA
            if keys[pg.K_a] and self.x > 0:
                # COLISÃO
                colide = colisao(pg.Rect(dx - VELOCIDADE, dy, PLAYER_LARGURA, PLAYER_ALTURA))
                if colide == False:
                    dx -= VELOCIDADE
        # RIGHT | DIREITA
            elif keys[pg.K_d] and self.x < LARGURA:
                # COLISÃO
                colide = colisao(pg.Rect(dx + VELOCIDADE, dy, PLAYER_LARGURA, PLAYER_ALTURA))
                if colide == False:
                    dx += VELOCIDADE

            if keys[pg.K_KP1]:
                cor = 'Yellow'

            if keys[pg.K_KP2]:
                cor = 'Green'
                
            if keys[pg.K_KP3]:
                cor = 'Blue'

            self.x = dx
            self.y = dy


    def draw(self) -> None:
        pg.draw.rect(self.game.Tela, cor, (self.x, self.y, PLAYER_LARGURA, PLAYER_ALTURA) )

