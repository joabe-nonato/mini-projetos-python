import pygame as pg
from util import *
from settings import *
from data import *

parado = []
frente = []
tras = []
agachado = []
pulo = []
pulo_frente = []
pulo_tras = []

animacao = [parado, frente, tras, agachado]

def carregar_personagem(self):
    spritesheet = pg.image.load(os.path.join(self.game.Imagens, self.personagem[0]))    
    # parado.append(self.personagem[1])

    for posicao in self.personagem[1]:
        imagem = spritesheet.subsurface(posicao)
        imagem = pg.transform.scale(imagem, (self.Bloco.w, self.Bloco.h))
        parado.append(imagem)

    for posicao in self.personagem[2]:
        imagem = spritesheet.subsurface(posicao)
        imagem = pg.transform.scale(imagem, (self.Bloco.w, self.Bloco.h))
        frente.append(imagem)

    for posicao in self.personagem[3]:
        imagem = spritesheet.subsurface(posicao)
        imagem = pg.transform.scale(imagem, (self.Bloco.w, self.Bloco.h))
        tras.append(imagem)

    for posicao in self.personagem[4]:
        imagem = spritesheet.subsurface(posicao)
        imagem = pg.transform.scale(imagem, (self.Bloco.w, self.Bloco.h))
        agachado.append(imagem)

    for posicao in self.personagem[5]:
        imagem = spritesheet.subsurface(posicao)
        imagem = pg.transform.scale(imagem, (self.Bloco.w, self.Bloco.h))
        pulo.append(imagem)

    for posicao in self.personagem[6]:
        imagem = spritesheet.subsurface(posicao)
        imagem = pg.transform.scale(imagem, (self.Bloco.w, self.Bloco.h))
        pulo_frente.append(imagem)

    reverter = self.personagem[6]
    for posicao in reverter[::-1]:
        imagem = spritesheet.subsurface(posicao)
        imagem = pg.transform.scale(imagem, (self.Bloco.w, self.Bloco.h))
        pulo_tras.append(imagem)

class Player02:
    def __init__(self, game) -> None:
        self.game = game                        
        self.Bloco = pg.Rect(((TELA_LARGURA // 2)), (TELA_ALTURA_CHAO - 250), 120, 250 )
        self.sprites = personagem[0]
        self.velx = 3
        self.vely = 6
        self.pulo = 0    
        self.esquerda = False
        self.limite_esquerdo = False
        self.limite_direito = False        
        self.saude = BARRA_ENERGIA            
        self.direcao = 0 #0 = parado, 1 = esquerda, 2 = direita, 3 = agacha, 4 = pulo


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
            # Diagonal Direita
            elif tecla[pg.K_UP] and self.pulo == 0 and tecla[pg.K_RIGHT]:
                self.pulo = 1
                self.direcao = 6
       
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
                # Agacha
                elif tecla[pg.K_DOWN] :            
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
            if self.Bloco.y > 30:
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
        redenderizar(self.game.Tela,'Red', self.Bloco)

        informacoes(self.game,'Red', f'P2 e:{self.esquerda} x:{self.Bloco.x} y:{self.Bloco.y} w:{self.Bloco.w} d:{self.direcao}', (TELA_LARGURA // 2), 100)
        
        # self.game.Tela.blit(self.sprites, self.Bloco)