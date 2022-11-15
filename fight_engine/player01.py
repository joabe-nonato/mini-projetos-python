import pygame as pg
from util import *
from settings import *
from data import *

class Player01:
    def __init__(self, game) -> None:
        self.game = game                          
        self.Bloco = pg.Rect(((TELA_LARGURA // 4)), (TELA_ALTURA_CHAO - 150), 80, 150 )
        self.sprites = pg.image.load(os.path.join(self.game.Imagens, ryu[0]))
        self.velx = 3
        self.vely = 6
        self.pulo = 0    
        self.esquerda = True
        self.limite_esquerdo = False
        self.limite_direito = False
        self.saude = BARRA_ENERGIA            
        self.direcao = 0 #0 = parado, 1 = esquerda, 2 = direita, 3 = agacha, 4 = pulo

    def eventos(self):
        self.esquerda = (self.Bloco.x < self.game.Player02.Bloco.x)
        self.limite_direito = False
        self.limite_esquerdo = False

        if self.game.Tempo > 0 and self.saude > 0 or TEMPO_LUTA == -99:
            tecla = pg.key.get_pressed()

            # Diagonal esquerda
            if tecla[pg.K_w] and self.pulo == 0 and tecla[pg.K_a]:
                self.pulo = 1
                self.direcao = 5
            # Diagonal Direita
            elif tecla[pg.K_w] and self.pulo == 0 and tecla[pg.K_d]:
                self.pulo = 1
                self.direcao = 6
                    
            if self.pulo == 0:  
                
                # Esquerda
                if tecla[pg.K_a]:                            
                    self.direcao = 1

                    #colisão esquerda
                    if self.esquerda == False and self.game.Player02.pulo == 0:
                        if self.Bloco.x <= (self.game.Player02.Bloco.x + self.game.Player02.Bloco.w):
                            self.direcao = 0
                            self.limite_esquerdo = True

                # Direita
                elif tecla[pg.K_d]:                     
                    self.direcao = 2

                    #colisão direita
                    if self.esquerda and self.game.Player02.pulo == 0:
                        if (self.Bloco.x + self.Bloco.w) >= self.game.Player02.Bloco.x:
                            self.direcao = 0
                            self.limite_direito = True                            
                else:
                    self.direcao = 0
                
                # Pulo
                if tecla[pg.K_w] :
                    self.pulo = 1
                    self.direcao = 4
                # Agacha
                elif tecla[pg.K_s] :
                    self.direcao = 3

    def atualizar(self):
        global dx
        global dy

        dx = self.Bloco.x
        dy = self.Bloco.y
        
        # esquerda direita        
        if self.direcao in [1,5] and dx > 0:
            dx -= self.velx
        elif self.direcao in [2,6] and dx < (TELA_LARGURA - self.Bloco.w):
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
        redenderizar(self.game.Tela,'Blue', self.Bloco)

        #adicionar Surface
        self.game.Tela.blit(pg.transform.scale(self.sprites, (self.Bloco.w, self.Bloco.h)), (self.Bloco.x, self.Bloco.y))


        informacoes(self.game,'Blue', f'P1 e:{self.esquerda} x:{self.Bloco.x} y:{self.Bloco.y} w:{self.Bloco.w} d:{self.direcao}', 10, 100)            
