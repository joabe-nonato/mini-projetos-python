from select import select
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
vitoria = []

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

    for posicao in self.personagem[7]:
        imagem = spritesheet.subsurface(posicao)
        imagem = pg.transform.scale(imagem, (self.Bloco.w, self.Bloco.h))
        vitoria.append(imagem)


class Player01:
    def __init__(self, game) -> None:
        self.game = game        
        self.indice = 0                  
        self.Bloco = pg.Rect(((TELA_LARGURA // 4)), (TELA_ALTURA_CHAO - 290), 180, 290 )
        self.personagem = personagem[0]        
        # self.sprites = self.Grupo()
        self.velx = 3
        self.vely = 6
        self.pulo = 0    
        self.esquerda = True
        self.limite_esquerdo = False
        self.limite_direito = False
        self.saude = BARRA_ENERGIA            
        self.direcao = 0 #0 = parado, 1 = esquerda, 2 = direita, 3 = agacha, 4 = pulo
        
        carregar_personagem(self)

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
        
        else:
            self.game.luta_encerrada = True

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
        sprites = pg.sprite.Group()  
        limite = 0  

        #adicionar Surface
        if self.direcao == 0:     
            limite = len(parado) - 1      
            if int(self.indice) > limite:
                self.indice = limite            
            sprt = pg.sprite.Sprite(sprites)        
            if self.esquerda:
                sprt.image = parado[int(self.indice)]
            else:
                sprt.image = pg.transform.flip(parado[int(self.indice)], True, False)
            sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y,5,5) 

        if self.direcao == 1:                         
            limite = len(tras) - 1         
            if int(self.indice) > limite:
                self.indice = limite
            sprt = pg.sprite.Sprite(sprites)      
            if self.esquerda:
                sprt.image = tras[int(self.indice)]
            else:
                sprt.image = pg.transform.flip(tras[int(self.indice)], True, False)
            sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h) 

        if self.direcao == 2:                         
            limite = len(frente) - 1         
            if int(self.indice) > limite:
                self.indice = limite
            sprt = pg.sprite.Sprite(sprites)         
            if self.esquerda:
                sprt.image = frente[int(self.indice)]
            else:
                sprt.image = pg.transform.flip(frente[int(self.indice)], True, False)
            sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h)        

        if self.direcao == 3:                         
            limite = len(agachado) - 1         
            if int(self.indice) > limite:
                self.indice = limite
            sprt = pg.sprite.Sprite(sprites)           
            if self.esquerda:
                sprt.image = agachado[int(self.indice)]
            else:
                sprt.image = pg.transform.flip(agachado[int(self.indice)], True, False)
            sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h) 

        if self.direcao == 4:                         
            limite = len(pulo) - 1         
            if int(self.indice) > limite:
                self.indice = limite
            sprt = pg.sprite.Sprite(sprites)       
            if self.esquerda:
                sprt.image = pulo[int(self.indice)]
            else:
                sprt.image = pg.transform.flip(pulo[int(self.indice)], True, False)
            sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h) 


        if self.direcao == 5:                         
            limite = len(pulo_tras) - 1         
            if int(self.indice) > limite:
                self.indice = limite
            sprt = pg.sprite.Sprite(sprites)            
            if self.esquerda:
                sprt.image = pulo_tras[int(self.indice)]
            else:
                sprt.image = pg.transform.flip(pulo_tras[int(self.indice)], True, False)
            sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h)

        if self.direcao == 6:                         
            limite = len(pulo_frente) - 1         
            if int(self.indice) > limite:
                self.indice = limite
            sprt = pg.sprite.Sprite(sprites)              
            if self.esquerda:
                sprt.image = pulo_frente[int(self.indice)]
            else:
                sprt.image = pg.transform.flip(pulo_frente[int(self.indice)], True, False)
            sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h)


        
        if self.game.luta_encerrada and self.Bloco.y == (TELA_ALTURA_CHAO - 290):
            limite = len(vitoria) - 1         
            if int(self.indice) > limite:
                self.indice = limite
            sprt = pg.sprite.Sprite(sprites)                                
            sprt.image = vitoria[int(self.indice)]
            sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h)

            if  int(self.indice) <= limite:
                self.indice += 0.1
            else:
                self.indice = limite
        else:
            if self.direcao == 3:
                if  self.indice < limite:
                    self.indice += 0.1
            elif self.direcao in [4,5,6]:
                if  self.indice < limite:
                    self.indice += 0.07
            else:
                if  self.indice > limite:
                    self.indice = 0
                else:
                    self.indice += 0.09
        
        sprites.draw(self.game.Tela)

        # imagemteste = pg.image.load(os.path.join(self.game.Imagens, "teste.png")).convert_alpha()
        # self.game.Tela.blit(pg.transform.scale(imagemteste, (self.Bloco.w + 60, self.Bloco.h + 60)), (self.Bloco.x - 60, self.Bloco.y - 60))

        redenderizar(self.game.Tela,'Blue', self.Bloco)
        informacoes(self.game,'Blue', f'P1 e:{self.esquerda} x:{self.Bloco.x} y:{self.Bloco.y} w:{self.Bloco.w} d:{self.direcao}', 10, 100)            
