import pygame as pg
from essencial import *
from settings import *
from data import *

selecionado = 1
personagem_altura_chao = (TELA_ALTURA_CHAO - 290)
spritesheet = ''

parado = []                 
frente = []                 
tras = []                   
agachado = []                   
pulo = []                   
pulo_frente = []
pulo_tras = []                  
vitoria = []                    
derrota = []                    
socoforte  = []                 
socomedia  = []                 
socofraco  = []                 
chuteforte = []                 
chutemedia = []                 
chutefraco = []                 
voadoraforte = []                   
voadoramedia = []                   
voadorafraco = []                   
especial01  = []                    
especial02  = []                    
especial03  = []                    
especial04  = []                    
especial05  = []                    
especial06  = []                    
especial07 = []                 
especial08 = []                 
especial09 = []                 
especial10 = []  

class Player02:
    def __init__(self, game) -> None:
        self.game = game             
        self.indice = 0             
        self.Bloco = pg.Rect(alinhar_centro(datap[selecionado].largura, TELA_CENTRO_V, False), TELA_ALTURA_CHAO - datap[selecionado].altura, datap[selecionado].largura, datap[selecionado].altura)
        self.personagem = personagem[selecionado]
        self.gravidade = (gravidade[selecionado] * -1)                                
        self.velocidade_x = velocidade_x[selecionado]
        self.velocidade_y = velocidade_y[selecionado]
        self.velocidade_xy = velocidade_xy[selecionado]
        self.teclaprecionada = False
        self.pulo = 0        
        self.esquerda = True
        self.limite_esquerdo = False
        self.limite_direito = False        
        self.saude = BARRA_ENERGIA            
        self.direcao = 0 #0 = parado, 1 = esquerda, 2 = direita, 3 = agacha, 4 = pulo

        global gravidadeY
        gravidadeY = gravidade[selecionado]
        animacao_comportamento(self, spritesheet, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, vitoria, derrota, socoforte , socomedia , socofraco , chuteforte, chutemedia, chutefraco, voadoraforte, voadoramedia, voadorafraco, especial01 , especial02 , especial03 , especial04 , especial05 , especial06 , especial07, especial08, especial09, especial10)

    def golpe(self, golpe):
        pass


    def eventos(self):        
        self.esquerda = (self.Bloco.x < self.game.Player01.Bloco.x)
        self.limite_direito = False
        self.limite_esquerdo = False

        if self.game.Tempo > 0 and self.saude > 0 or TEMPO_LUTA == -99:
            tecla = pg.key.get_pressed()

            # Diagonal esquerda
            if tecla[pg.K_UP] and self.pulo == 0 and tecla[pg.K_LEFT]:
                self.pulo = 1
                self.direcao = 5
                if self.Bloco.y == personagem_altura_chao:  
                    self.indice = 0
            # Diagonal Direita
            elif tecla[pg.K_UP] and self.pulo == 0 and tecla[pg.K_RIGHT]:
                self.pulo = 1
                self.direcao = 6
                if self.Bloco.y == personagem_altura_chao:  
                    self.indice = 0
       
            if self.pulo == 0:  
                                
                # Esquerda
                if tecla[pg.K_LEFT]:                            
                    self.direcao = 1

                    #colisão esquerda
                    if self.esquerda == False and self.game.Player01.pulo == 0:
                        if self.Bloco.x <= (self.game.Player01.Bloco.x + self.game.Player01.Bloco.w):
                            self.direcao = 0
                            self.limite_esquerdo = True
                # Direita
                elif tecla[pg.K_RIGHT]:                            
                    self.direcao = 2

                    #colisão direita
                    if self.esquerda and self.game.Player01.pulo == 0:
                        if (self.Bloco.x + self.Bloco.w) >= self.game.Player01.Bloco.x:
                            self.direcao = 0
                            self.limite_direito = True        
                else:
                    self.direcao = 0

                # Pulo
                if tecla[pg.K_UP] :
                    self.pulo = 1
                    self.direcao = 4
                    self.indice = 0
                # Agacha
                elif tecla[pg.K_DOWN] :            
                    self.direcao = 3     

        else:
            self.game.luta_encerrada = True
            self.direcao = 0               

    def atualizar(self):
        aplicar_movimentacao(self, gravidadeY)        
        # global dx
        # global dy

        # dx = self.Bloco.x
        # dy = self.Bloco.y
        
        # # esquerda direita
        # if self.direcao in [1,5] and dx > 0:
        #     dx -= self.velocidade_x
        # elif self.direcao in [2,6] and dx < (TELA_LARGURA - self.Bloco.w):
        #     dx += self.velocidade_x        

        # #pulo
        # if self.pulo == 1:
        #     if self.Bloco.y > 30:
        #         dy -= self.velocidade_y
        #     else:
        #         self.pulo = 2
        
        # if self.pulo == 2:
        #     if dy < (TELA_ALTURA_CHAO - self.Bloco.h):
        #         dy += self.velocidade_y
        #     else:
        #         self.pulo = 0        
        #         self.direcao = 0
                   
        # self.Bloco.x = dx
        # self.Bloco.y = dy

    def desenhar(self):  
        # executar animações
        sprites = pg.sprite.Group()  
        animacao(self, sprites, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, vitoria, derrota, socoforte , socomedia , socofraco , chuteforte, chutemedia, chutefraco, voadoraforte, voadoramedia, voadorafraco, especial01 , especial02 , especial03 , especial04 , especial05 , especial06 , especial07, especial08, especial09, especial10)
        sprites.draw(self.game.Tela)


        redenderizar(self.game.Tela,'Red', self.Bloco)

        informacoes(self.game,'Red', f'P2 e:{self.esquerda} x:{self.Bloco.x} y:{self.Bloco.y} w:{self.Bloco.w} d:{self.direcao} g:{self.gravidade}', (TELA_LARGURA // 2), 100)
        
        # self.game.Tela.blit(self.sprites, self.Bloco)