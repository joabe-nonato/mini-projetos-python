import pygame as pg
from util import *
from settings import *
from data import *

class Player02:
    def __init__(self, game) -> None:
        self.game = game                        
        self.Bloco = ryu[0]
        self.sprites = ryu[1]
        self.velx = 3
        self.vely = 6
        self.pulo = 0    
        self.saude = BARRA_ENERGIA            
        self.direcao = 0 #0 = parado, 1 = esquerda, 2 = direita

    def eventos(self):
        if self.game.Tempo > 0 and self.saude > 0 or TEMPO_LUTA == -99:
            tecla = pg.key.get_pressed()

            # Diagonal esquerda
            if tecla[pg.K_w] and self.pulo == 0 and tecla[pg.K_a]:
                self.pulo = 1
                self.direcao = 1
            # Diagonal Direita
            elif tecla[pg.K_w] and self.pulo == 0 and tecla[pg.K_d]:
                self.pulo = 1
                self.direcao = 2

            # Pulo
            if tecla[pg.K_w] and self.pulo == 0 :
                self.pulo = 1
            # Agacha
            elif tecla[pg.K_s] and dy < (TELA_ALTURA - self.Bloco.h):            
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

        dx = self.Bloco.x
        dy = self.Bloco.y
        
        # esquerda direita
        if self.direcao == 1 and dx > 0:
            dx -= self.velx
        elif self.direcao == 2 and dx < (TELA_LARGURA - self.Bloco.w):
            dx += self.velx        

        #pulo
        if self.pulo == 1:
            if self.Bloco.y > self.Bloco.h:
                dy -= self.vely
            else:
                self.pulo = 2
        
        if self.pulo == 2:
            if dy < (TELA_ALTURA_CHAO - self.Bloco.h):
                dy += self.vely
            else:
                self.pulo = 0        
                self.direcao = 0
                   
        self.Bloco.x = dx
        self.Bloco.y = dy

    def desenhar(self):                                
        redenderizar(self.game.Tela,'Red', (self.Bloco.x,self.Bloco.y, self.Bloco.w, self.Bloco.h))

        if DEBUG:
            msg = f'x:{self.Bloco.x} y:{self.Bloco.y}'
            texto = self.game.fonte.render(msg, True, 'Red')        
            self.game.Tela.blit(texto, (self.Bloco.x + 5, self.Bloco.y))

            chaotext = f'chao:{(TELA_ALTURA - (TELA_ALTURA_CHAO - self.Bloco.h))}'
            texto = self.game.fonte.render(chaotext, True, 'Red')                
            self.game.Tela.blit(texto, (self.Bloco.x, (TELA_ALTURA_CHAO ) ))
        
        # self.game.Tela.blit(self.sprites, self.Bloco)