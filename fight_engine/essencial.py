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



# APLICAR MOVIMENTAÇÃO        
def aplicar_movimentacao(self, oponente):
    # global dx
    # global dy
    gravidadeY = self.gravidadeY
    dx = self.BlocoMov.x
    dy = self.BlocoMov.y
    
    colide = pg.Rect.colliderect(self.BlocoMov, oponente.BlocoMov)
    
    if self.golpe == 0 and self.movimento not in [14, 15]:
        # esquerda
        if self.movimento in [1] and dx > 0:
            dx -= self.velocidade_x
        # direita        
        elif self.movimento in [2] and dx < (TELA_LARGURA - self.BlocoMov.w):
            dx += self.velocidade_x
        
    #pulo diagonal
    if self.pulo:
        if self.movimento in [5] and dx > 0:
            dx -= self.velocidade_xy
    # direita        
        elif self.movimento in [6] and dx < (TELA_LARGURA - self.BlocoMov.w):
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
               
# AFASTAR AO SER GOLPEADO
    if self.movimento in [14, 15] and dx > 0:        
        if self.esquerda:
            dx -= (self.velocidade_x * 2.3)
        elif dx < (TELA_LARGURA - self.BlocoMov.w):
            dx += (self.velocidade_x * 2.3)

    if colide and self.BlocoMov.bottom == self.game.chao and oponente.BlocoMov.bottom == self.game.chao: 
        if oponente.movimento == 0:
            if self.esquerda:
                oponente.BlocoMov.x = (self.BlocoMov.w + dx)
            else:
                oponente.BlocoMov.right = self.BlocoMov.left
    else:        
        self.BlocoMov.x = dx
        self.BlocoMov.y = dy

# RECUPERAR ENTRADA DE COMANDOS
def monitorar_golpes(self, evg):
    
    tecla = 0

    if self.game.luta_encerrada == False and self.golpe == 0:
        # self.movimento = 0

        if evg.type == pg.KEYDOWN:
            tecla = evg.key
            
            # 7 : socoforte 
            if tecla == self.tecla_soco and self.movimento in [0,1,2]:                
                self.golpe = 7
                self.indice = 0

            # 8 : socoagachado
            if tecla == self.tecla_soco and self.movimento in [3]:
                self.golpe = 8
                self.indice = 0

            # 9 : chuteforte
            if tecla == self.tecla_chute and self.movimento in [0,1,2] :
                self.golpe = 9
                self.indice = 0

            # 10 : chuteagachado
            if tecla == self.tecla_chute and self.movimento in [3] :
                self.golpe = 10
                self.indice = 0

            # 11 : voadoradiagonal
            if tecla == self.tecla_chute and self.movimento in [5,6]:
                self.golpe = 11
                self.indice = 0

            # 12 : voadoravertical
            if tecla == self.tecla_chute and self.movimento in [4]:
                self.golpe = 12
                self.indice = 0

            # 13 : socoaereo
            if tecla == self.tecla_soco and self.movimento in [4,5,6]:
                self.golpe = 13
                self.indice = 0
        

# MOVIMENTOS
def monitorar_movimentos(self):
    
    pressionando = pg.key.get_pressed()
    tecla = 0

    if self.game.luta_encerrada == False and self.golpe == 0:
    # Diagonal esquerda
            if self.pulo == 0 and pressionando[self.tecla_cima] and pressionando[self.tecla_esquerda]:
                self.pulo = 1
                self.movimento = 5     
                if self.BlocoMov.bottom == self.game.chao:  
                    self.indice = 0         
    # Diagonal Direita
            elif self.pulo == 0 and pressionando[self.tecla_cima] and pressionando[self.tecla_direita]:
                self.pulo = 1
                self.movimento = 6
                if self.BlocoMov.bottom == self.game.chao:  
                    self.indice = 0
                    
            if self.pulo == 0:  
                # Esquerda
                if tecla == self.tecla_esquerda or pressionando[self.tecla_esquerda]:
                    self.movimento = 1
                # Direita
                elif tecla == self.tecla_direita or pressionando[self.tecla_direita]:
                    self.movimento = 2
                else:
                    self.movimento = 0                    
                # Pulo
                if tecla == self.tecla_cima or pressionando[self.tecla_cima]:                    
                    self.pulo = 1                    
                    self.movimento = 4
                    self.indice = 0
                # Agacha
                elif tecla == self.tecla_baixo or pressionando[self.tecla_baixo]:
                    self.movimento = 3         
    
    elif self.pulo == 0 and self.golpe == 0:
    # else:
        self.golpe = 0
        self.movimento = 0
        self.indice = 0
