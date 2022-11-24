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
        pg.draw.rect(self.game.superficie, cor, self.BlocoMov, 2)        
        # pg.draw.rect(self.game.superficie, cor, self.BlocoImagem, 2)
        pg.draw.rect(self.game.superficie, VERDE, self.bloco_golpe)

# def criarobjeto(posx, posy, larg, alt, velocidade_x = 1, velocidade_y = 1):
#     return [pg.Rect(posx, posy, larg, alt), [velocidade_x, velocidade_y]]

# def colisalateral(eesquerda, movimento, bloco_esquerda, bloco_direita):
#     if eesquerda:
#         if (bloco_esquerda.x + bloco_esquerda.w) >= bloco_direita.x:
#             return 0
#     else:
#         if bloco_esquerda.x <= (bloco_direita.x + bloco_direita.w):
#             return 0
    
#     return movimento

def informacoes(game, cor, msg, left, topo):
    if DEBUG:
        linhas = msg.split(' ')            
        for escrever in linhas:
            texto = game.fonte.render(escrever, True, cor)                        
            game.superficie.blit(texto, (left , topo))
            topo += 17


# LISTAS DE IMAGENS POR MOVIMENTOS
def carregar_movimentos(self, spritesheet, lista_origem, lista_destino):
        for frame in lista_origem:
            # RECUPERA IMAGEM
            imagem = spritesheet.subsurface(frame[0])        

            # RECUPERA O TAMANHO DA IMAGEM
            transform = (0,0,0,0)
            if len(frame) > 0:
                transform = frame[1]

            #GOLPE
            golpe = (0,0,0,0)
            if len(frame) > 2:
                golpe = frame[2] 
            
            lista_destino.append([imagem, transform, golpe])

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

        
        centro_bloco = (self.BlocoMov.x + (self.BlocoMov.w // 2))
        
        sprt = pg.sprite.Sprite(sprites)
        transform = ((0,0),(0,0))
        
        def calcular_limite(lista):
            lmt = len(lista) - 1      
            if int(self.indice) > lmt:
                self.indice = lmt
            return lmt
                

        def executar_golpe(lista_golpe):
            if len(socoforte[int(self.indice)]):
                self.bloco_golpe = pg.Rect(socoforte[int(self.indice)][2])
                self.bloco_golpe.center + self.BlocoImagem.center
                self.bloco_golpe.y = (self.BlocoImagem.y + self.bloco_golpe.y)

                if self.esquerda:
                    self.bloco_golpe.x = (self.bloco_golpe.x + self.BlocoImagem.centerx)
                else:
                    self.bloco_golpe.x = ((self.bloco_golpe.x * -1) + self.BlocoImagem.x)
                

        def retorno_padrao(sprt):            
            blc = pg.Rect(0, 0 , sprt.image.get_width(), sprt.image.get_height())
            blc.centerx = self.BlocoMov.centerx
            blc.bottom = self.BlocoMov.bottom
            
            return blc


        def retorno_imagem(esquerda, posicao_imagem):            
            imagemLocal = posicao_imagem[0]
            imagemLocal = pg.transform.scale(imagemLocal, (sprt.rect.w, sprt.rect.h))

            if esquerda == False:
                imagemLocal = pg.transform.flip(imagemLocal, True, False)

            return imagemLocal


        def retorno_retangulo(esquerda, posicao_tamanho):  
            blocoimg = posicao_tamanho[1]          

            self.BlocoImagem = pg.Rect(0, 0, blocoimg[0], blocoimg[1])               
            
            # self.BlocoImagem.centerx = self.BlocoMov.centerx
            self.BlocoImagem.bottom = self.BlocoMov.bottom
                        
            if self.esquerda:
                self.BlocoImagem.left = self.BlocoMov.left
            else:
                self.BlocoImagem.right = self.BlocoMov.right

            return self.BlocoImagem

        def esquerda_direita(esquerda, direita):
            if self.esquerda:
                return esquerda
            else:
                return direita        

                
#ANIMAÇÃO - IDENTIFICAR QUAL MOVIMENTO
        generico = parado

        # PARADO
        if self.movimento == 0: 
            generico = parado

        if self.movimento == 1: 
            generico = esquerda_direita(tras, frente)

        if self.movimento == 2: 
            generico = esquerda_direita(frente, tras)
        
        if self.movimento == 3: 
            generico = agachado
        
        if self.movimento == 4: 
            generico = pulo
        
        if self.movimento == 5: 
            generico = esquerda_direita(pulo_tras, pulo_frente)
        
        if self.movimento == 6: 
            generico = esquerda_direita(pulo_frente, pulo_tras)

        if self.movimento == 10: 
            generico = socoforte           

        if self.movimento == 11:
            generico = socoagachado

        if self.golpe:
            executar_golpe(generico)

        limite = calcular_limite(generico)
        sprt.rect = retorno_retangulo(self.esquerda, generico[int(self.indice)])
        sprt.image = retorno_imagem(self.esquerda, generico[int(self.indice)])
        

####################################################################
        if self.golpe:
            if  self.indice < limite:
                self.indice += 0.5
            elif self.movimento in [11] :
                # self.indice = 0
                # self.movimento = 0
                self.golpe = False
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
        
def aplicar_movimentacao(self, gravidadeY, oponente):
    global dx
    global dy
    dx = self.BlocoMov.x
    dy = self.BlocoMov.y

    colisao_direita = (int(self.BlocoMov.right) == int(oponente.BlocoMov.left))
    colisao_esquerda = (int(oponente.BlocoMov.right) == int(self.BlocoMov.left))
    
    # esquerda 
    if self.movimento in [1] and dx > 0:        
        if colisao_esquerda == False:
            dx -= self.velocidade_x
     # direita        
    elif self.movimento in [2] and dx < (TELA_LARGURA - self.BlocoMov.w):
        if colisao_direita == False:
            dx += self.velocidade_x        
    
    #pulo diagonal
    if self.movimento in [5] and dx > 0:
        if colisao_esquerda == False:
            dx -= self.velocidade_xy
     # direita        
    elif self.movimento in [6] and dx < (TELA_LARGURA - self.BlocoMov.w):
        if colisao_direita == False:
            dx += self.velocidade_xy

    #pulo reto
    if self.pulo == 1:
        self.gravidade += self.velocidade_y
        dy += int(self.gravidade)
        
        if self.gravidade >= gravidadeY:        
            self.pulo = 0        
            self.movimento = 0
            self.gravidade = (gravidadeY * -1)
            dy = (self.game.chao - self.BlocoMov.h)
               
    
    self.BlocoMov.x = dx
    self.BlocoMov.y = dy

    colisao_esquerda = False
    colisao_direita = False
    

def monitorar_teclas_movimento(self, oponente):

        tecla = pg.key.get_pressed()

        if self.golpe == False:
        # Diagonal esquerda
                if tecla[self.tecla_cima] and self.pulo == 0 and tecla[self.tecla_esquerda]:                
                    self.pulo = 1
                    self.movimento = 5     
                    if self.BlocoMov.bottom == self.game.chao:  
                        self.indice = 0         
        # Diagonal Direita
                elif tecla[self.tecla_cima] and self.pulo == 0 and tecla[self.tecla_direita]:
                    self.pulo = 1
                    self.movimento = 6
                    if self.BlocoMov.bottom == self.game.chao:  
                        self.indice = 0
                        
                if self.pulo == 0:  
                    # Esquerda
                    if tecla[self.tecla_esquerda]:
                        self.movimento = 1
                        #colisão esquerda
                        # if self.esquerda == False and oponente.pulo == 0:
                        #     if self.BlocoMov.x <= (oponente.BlocoMov.x + oponente.BlocoMov.w):
                        #         # self.movimento = 0                                
                        #         colisao_esquerda = True
                    # Direita
                    elif tecla[self.tecla_direita]:                     
                        self.movimento = 2
                        #colisão direita
                        # if self.esquerda and oponente.pulo == 0:
                        #     if (self.BlocoMov.x + self.BlocoMov.w) >= oponente.BlocoMov.x:
                        #         # self.movimento = 0     
                        #         colisao_direita  = False                       
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
        