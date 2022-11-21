from tkinter import CENTER
import pygame as pg
import os
from settings import *


def alinhar_centro(largura, destino, esquerda = True):
    if esquerda:
        return ((destino - largura) / 2)
    else:
        return destino + ((destino - largura) / 2)

def redenderizar(self, cor):
    if DEBUG:
        pg.draw.rect(self.game.Tela, cor, self.Bloco, 2)
        pg.draw.rect(self.game.Tela, VERMELHO, self.bloco_golpe, 3)

def criarobjeto(posx, posy, larg, alt, velocidade_x = 1, velocidade_y = 1):
    return [pg.Rect(posx, posy, larg, alt), [velocidade_x, velocidade_y]]

def colisalateral(eesquerda, movimento, bloco_esquerda, bloco_direita):
    if eesquerda:
        if (bloco_esquerda.x + bloco_esquerda.w) >= bloco_direita.x:
            return 0
    else:
        if bloco_esquerda.x <= (bloco_direita.x + bloco_direita.w):
            return 0
    
    return movimento

def informacoes(game, cor, msg, left, topo):
    if DEBUG:
        linhas = msg.split(' ')            
        for escrever in linhas:
            texto = game.fonte.render(escrever, True, cor)                        
            game.Tela.blit(texto, (left , topo))
            topo += 17


# LISTAS DE IMAGENS POR MOVIMENTOS
def carregar_movimentos(self, spritesheet, lista_origem, lista_destino):
        for frame in lista_origem:
            # RECUPERA IMAGEM
            imagem = spritesheet.subsurface(frame[0])        

            if len(frame) > 0:
            # RECUPERA O TAMANHO DA IMAGEM
                imagem = pg.transform.scale(imagem, frame[1])            

            #GOLPE
            golpe = (0,0,0,0)
            if len(frame) > 2:
                golpe = frame[2] 
            
            lista_destino.append([imagem, golpe])

def animacao_comportamento(self, spritesheet, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, vitoria, derrota, socoforte, socoagachado , socomedia , socofraco , chuteforte, chutemedia, chutefraco, voadoraforte, voadoramedia, voadorafraco, especial01 , especial02 , especial03 , especial04 , especial05 , especial06 , especial07, especial08, especial09, especial10):
   
# RECUPERAR TODAS AS IMAGENS
    spritesheet = pg.image.load(os.path.join(self.game.Imagens, self.spritesheet))    
    
# PARADO
    carregar_movimentos(self, spritesheet, self.personagem[0], parado)    
# FRENTE
    carregar_movimentos(self, spritesheet, self.personagem[1], frente)    
# TRAS
    carregar_movimentos(self, spritesheet, self.personagem[2], tras)    
# AGACHADO
    carregar_movimentos(self, spritesheet, self.personagem[3], agachado)    
# PULO RETO
    carregar_movimentos(self, spritesheet, self.personagem[4], pulo)    
# PULO FRENTE
    carregar_movimentos(self, spritesheet, self.personagem[5], pulo_frente)
# PULO TRAS
    carregar_movimentos(self, spritesheet, self.personagem[5][::-1], pulo_tras)    

# SOCO FORTE
    carregar_movimentos(self, spritesheet, self.personagem[7], socoforte)
# SOCO AGACHADO
    carregar_movimentos(self, spritesheet, self.personagem[8], socoagachado)

# VITORIA
    # carregar_movimentos(self, spritesheet, self.personagem[6], vitoria)


def animacao(self, sprites, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, vitoria, derrota, socoforte, socoagachado , socomedia , socofraco , chuteforte, chutemedia, chutefraco, voadoraforte, voadoramedia, voadorafraco, especial01 , especial02 , especial03 , especial04 , especial05 , especial06 , especial07, especial08, especial09, especial10):          
        
        limite = 0  

        
        centro_bloco = (self.Bloco.x + (self.Bloco.w // 2))
        
        sprt = pg.sprite.Sprite(sprites)
        
        def calcular_limite(lista):
            lmt = len(lista) - 1      
            if int(self.indice) > lmt:
                self.indice = lmt
            return lmt
                
        def retorno_padrao(sprt):
            return pg.Rect(self.Bloco.x, TELA_ALTURA_CHAO - int(sprt.image.get_height()) , self.Bloco.w ,self.Bloco.h)

        
        if self.movimento == 10: 
            limite = calcular_limite(socoforte)
            if self.esquerda:
                sprt.image = socoforte[int(self.indice)][0]               
            else:
                sprt.image = pg.transform.flip(socoforte[int(self.indice)][0], True, False)   

            sprt.rect = retorno_padrao(sprt)

            if len(socoforte[int(self.indice)]):
                    self.bloco_golpe = pg.Rect(socoforte[int(self.indice)][1])
                    self.bloco_golpe.y = (self.Bloco.y + self.bloco_golpe.y)

                    if self.esquerda:
                        self.bloco_golpe.x = centro_bloco
                    else:
                        self.bloco_golpe.x = self.Bloco.x - self.Bloco.w + self.bloco_golpe.x
                    
                    pg.draw.rect(self.game.Tela, VERMELHO, self.bloco_golpe, 3)

        if self.movimento == 11: 
            limite = calcular_limite(socoagachado)
            sprt.image = socoagachado[int(self.indice)][0]               
            sprt.rect = retorno_padrao(sprt)

            if len(socoagachado[int(self.indice)]):
                    self.bloco_golpe = pg.Rect(socoagachado[int(self.indice)][1])
                    self.bloco_golpe.y = (self.Bloco.y + self.bloco_golpe.y)

                    if self.esquerda:
                        self.bloco_golpe.x = centro_bloco
                    else:
                        self.bloco_golpe.x = self.Bloco.x - self.Bloco.w + self.bloco_golpe.x

                    pg.draw.rect(self.game.Tela, VERMELHO, self.bloco_golpe, 3)  

                
        #Animação        
        if self.esquerda:

            if self.movimento == 0:                     
                # aplicar_animacao(self, parado, sprites)
                limite = calcular_limite(parado)
                sprt.image = parado[int(self.indice)][0]                
                sprt.rect = retorno_padrao(sprt)
 
            if self.movimento == 1:                         
                limite = calcular_limite(tras)
                sprt.image = tras[int(self.indice)][0]
                sprt.rect = retorno_padrao(sprt)

            if self.movimento == 2:                         
                limite = calcular_limite(frente)
                sprt.image = frente[int(self.indice)][0]
                sprt.rect = retorno_padrao(sprt)

            if self.movimento == 3:                         
                limite = calcular_limite(agachado)
                sprt.image = agachado[int(self.indice)][0]
                sprt.rect = retorno_padrao(sprt)

            if self.movimento == 4:                         
                limite = calcular_limite(pulo)
                sprt.image = pulo[int(self.indice)][0]
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h)

            if self.movimento == 5:                         
                limite = calcular_limite(pulo_tras)
                sprt.image = pulo_tras[int(self.indice)][0]
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h)

            if self.movimento == 6:                         
                limite = calcular_limite(pulo_frente)                 
                sprt.image = pulo_frente[int(self.indice)][0]
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h)
        else:
            if self.movimento == 0:     
                limite = calcular_limite(parado)
                sprt.image = pg.transform.flip(parado[int(self.indice)][0], True, False)
                sprt.rect = retorno_padrao(sprt)
            
            if self.movimento == 2:                         
                limite = calcular_limite(tras)
                sprt.image = pg.transform.flip(tras[int(self.indice)][0], True, False)
                sprt.rect = retorno_padrao(sprt)

            if self.movimento == 1:                         
                limite = calcular_limite(frente)
                sprt.image = pg.transform.flip(frente[int(self.indice)][0], True, False)
                sprt.rect = retorno_padrao(sprt) 

            if self.movimento == 3:                         
                limite = calcular_limite(agachado)
                sprt.image = pg.transform.flip(agachado[int(self.indice)][0], True, False)
                sprt.rect = retorno_padrao(sprt)

            if self.movimento == 4:                         
                limite = calcular_limite(pulo)
                sprt.image = pg.transform.flip(pulo[int(self.indice)][0], True, False)
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h) 

            if self.movimento == 6:                         
                limite = calcular_limite(pulo_tras)
                sprt.image = pg.transform.flip(pulo_tras[int(self.indice)][0], True, False)
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h)

            if self.movimento == 5:                         
                limite = calcular_limite(pulo_frente)
                sprt.image = pg.transform.flip(pulo_frente[int(self.indice)][0], True, False)
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h)

        # sprt.rect.center = (self.Bloco.w  - self.Bloco.x ,self.Bloco.h //2)

        if self.golpe:
            if  self.indice < limite:
                self.indice += 1
            else:
                self.indice = 0
                self.movimento = 0
                self.golpe = False
        # agachar e pulo 
        elif self.movimento in [3]:
            if  self.indice < limite:
                self.indice += 0.1
        elif self.movimento in [4]:
            if  self.indice < limite:
                self.indice += 1
        # pulo diagonal
        elif self.movimento in [5,6]:
            if  self.indice < limite:
                self.indice += 0.15
        # direta esquerda
        else:
            if  self.indice > limite:
                self.indice = 0
            else:
                self.indice += 0.1
        
def aplicar_movimentacao(self, gravidadeY):
    global dx
    global dy
    dx = self.Bloco.x
    dy = self.Bloco.y
    
    # esquerda 
    if self.movimento in [1] and dx > 0:
        dx -= self.velocidade_x
     # direita        
    elif self.movimento in [2] and dx < (TELA_LARGURA - self.Bloco.w):
        dx += self.velocidade_x        
    
    #pulo diagonal
    if self.movimento in [5] and dx > 0:
        dx -= self.velocidade_xy
     # direita        
    elif self.movimento in [6] and dx < (TELA_LARGURA - self.Bloco.w):
        dx += self.velocidade_xy

    #pulo reto
    if self.pulo == 1:
        self.gravidade += self.velocidade_y
        dy += int(self.gravidade)
        
        if self.gravidade >= gravidadeY:        
            self.pulo = 0        
            self.movimento = 0
            self.gravidade = (gravidadeY * -1)
            dy = (TELA_ALTURA_CHAO - self.Bloco.h)
               
    self.Bloco.x = dx
    self.Bloco.y = dy

    # if self.golpe:
    #     self.indice += 1
    # else:
    #     self.indice = 0
    #     self.movimento = 0
    #     self.golpe = False


def monitorar_teclas_movimento(self, oponente):

        personagem_altura_chao = (TELA_ALTURA_CHAO - self.Bloco.height)

        tecla = pg.key.get_pressed()

        if self.golpe == False:
        # Diagonal esquerda
                if tecla[self.tecla_cima] and self.pulo == 0 and tecla[self.tecla_esquerda]:                
                    self.pulo = 1
                    self.movimento = 5     
                    if self.Bloco.y == personagem_altura_chao:  
                        self.indice = 0         
        # Diagonal Direita
                elif tecla[self.tecla_cima] and self.pulo == 0 and tecla[self.tecla_direita]:
                    self.pulo = 1
                    self.movimento = 6
                    if self.Bloco.y == personagem_altura_chao:  
                        self.indice = 0
                        
                if self.pulo == 0:  
                    # Esquerda
                    if tecla[self.tecla_esquerda]:
                        self.movimento = 1
                        #colisão esquerda
                        if self.esquerda == False and oponente.pulo == 0:
                            if self.Bloco.x <= (oponente.Bloco.x + oponente.Bloco.w):
                                self.movimento = 0
                    # Direita
                    elif tecla[self.tecla_direita]:                     
                        self.movimento = 2
                        #colisão direita
                        if self.esquerda and oponente.pulo == 0:
                            if (self.Bloco.x + self.Bloco.w) >= oponente.Bloco.x:
                                self.movimento = 0                            
                    else:
                        self.movimento = 0
                    
                    # Pulo
                    if tecla[self.tecla_cima] :                    
                        self.pulo = 1                    
                        self.movimento = 4
                        self.indice = 0
                    # Agacha
                    elif tecla[self.tecla_baixo] :
                        self.movimento = 3         
        