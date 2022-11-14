import pygame as pg
from util import *
from settings import *
from data import *

class Player01:
    def __init__(self, game) -> None:
        self.game = game                        
        self.P1 = ryu[0]
        self.velx = 3
        self.vely = 6
        self.pulo = 0                
        self.direcao = 0 #0 = parado, 1 = esquerda, 2 = direita
        # self.chao = pg.image.load("D:\PROJETOS\Python\dinogame\imagens\chao.png")

    def eventos(self):
        tecla = pg.key.get_pressed()

         # Diagonal esquerda
        if tecla[pg.K_w] and self.pulo == 0 and tecla[pg.K_a]:
            self.pulo = 1
            self.direcao = 1
        # Diagonal Direita
        elif tecla[pg.K_w] and self.pulo == 0 and tecla[pg.K_d]:
            self.pulo = 1
            self.direcao = 2

        # Sobe
        if tecla[pg.K_w] and self.pulo == 0 :
            self.pulo = 1
        # Desce
        elif tecla[pg.K_s] and dy < (TELA_ALTURA - self.P1.h):            
            self.direcao = 3
       
        if self.pulo == 0:  
            # Esquerda
            if tecla[pg.K_a]:                            
                self.direcao = 1
            # Direita
            elif tecla[pg.K_d]:                            
                self.direcao = 2
            else:
                self.direcao = 0

    def atualizar(self):
        global dx
        global dy

        dx = self.P1.x
        dy = self.P1.y
        
        # esquerda direita
        if self.direcao == 1 and dx > 0:
            dx -= self.velx
        elif self.direcao == 2 and dx < (TELA_LARGURA - self.P1.w):
            dx += self.velx        

        #pulo
        if self.pulo == 1:
            if self.P1.y > self.P1.h:
                dy -= self.vely
            else:
                self.pulo = 2
        
        if self.pulo == 2:
            if dy < (TELA_ALTURA_CHAO - self.P1.h):
                dy += self.vely
            else:
                self.pulo = 0        
                self.direcao = 0
                   
        self.P1.x = dx
        self.P1.y = dy

    def desenhar(self):                                
        redenderizar(self.game.Tela,'Blue', (self.P1.x,self.P1.y, self.P1.w, self.P1.h))

        if DEBUG:
            msg = f'x:{self.P1.x} y:{self.P1.y}'
            texto = self.game.fonte.render(msg, True, 'Red')        
            self.game.Tela.blit(texto, (self.P1.x + 5, self.P1.y))

            chaotext = f'chao:{(TELA_ALTURA - (TELA_ALTURA_CHAO - self.P1.h))}'
            texto = self.game.fonte.render(chaotext, True, 'Red')                
            self.game.Tela.blit(texto, (self.P1.x, (TELA_ALTURA_CHAO ) ))