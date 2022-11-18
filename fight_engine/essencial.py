import pygame as pg
import os
from settings import *

def redenderizar(t, cor, objt):
    if DEBUG:
        pg.draw.rect(t, cor, objt, 2)

def criarobjeto(posx, posy, larg, alt, velocidade_x = 1, velocidade_y = 1):
    return [pg.Rect(posx, posy, larg, alt), [velocidade_x, velocidade_y]]

def colisalateral(eesquerda, direcao, bloco_esquerda, bloco_direita):
    if eesquerda:
        if (bloco_esquerda.x + bloco_esquerda.w) >= bloco_direita.x:
            return 0
    else:
        if bloco_esquerda.x <= (bloco_direita.x + bloco_direita.w):
            return 0
    
    return direcao

def informacoes(game, cor, msg, left, topo):
    if DEBUG:
        linhas = msg.split(' ')            
        for escrever in linhas:
            texto = game.fonte.render(escrever, True, cor)                        
            game.Tela.blit(texto, (left , topo))
            topo += 17


# LISTAS DE IMAGENS POR MOVIMENTOS
def carregar_movimentos(self, spritesheet, lista_origem, lista_destino):
        for posicao in lista_origem:
            imagem = spritesheet.subsurface(posicao[0])        
            imagem = pg.transform.scale(imagem, posicao[1])
            lista_destino.append(imagem)

def animacao_comportamento(self, spritesheet, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, vitoria, derrota, socoforte , socomedia , socofraco , chuteforte, chutemedia, chutefraco, voadoraforte, voadoramedia, voadorafraco, especial01 , especial02 , especial03 , especial04 , especial05 , especial06 , especial07, especial08, especial09, especial10):
   
# RECUPERAR TODAS AS IMAGENS
    spritesheet = pg.image.load(os.path.join(self.game.Imagens, self.personagem[0]))    
    
# PARADO
    carregar_movimentos(self, spritesheet, self.personagem[1], parado)    
# FRENTE
    carregar_movimentos(self, spritesheet, self.personagem[2], frente)    
# TRAS
    carregar_movimentos(self, spritesheet, self.personagem[3], tras)    
# AGACHADO
    carregar_movimentos(self, spritesheet, self.personagem[4], agachado)    
# PULO RETO
    carregar_movimentos(self, spritesheet, self.personagem[5], pulo)    
# PULO FRENTE
    carregar_movimentos(self, spritesheet, self.personagem[6], pulo_frente)
# PULO TRAS
    carregar_movimentos(self, spritesheet, self.personagem[6][::-1], pulo_tras)    
# VITORIA
    carregar_movimentos(self, spritesheet, self.personagem[7], vitoria)
# SOCOFORTE
    carregar_movimentos(self, spritesheet, self.personagem[10], socoforte)

# EXECUTAR ANIMAÇÕES
# def aplicar_animacao(self, lista_origem, sprites):
#     limite = len(lista_origem) - 1      
#     if int(self.indice) > limite:
#         self.indice = limite            
#     sprt = pg.sprite.Sprite(sprites)        
#     sprt.image = lista_origem[int(self.indice)]
#     sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h) 

def animacao(self, sprites, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, vitoria, derrota, socoforte , socomedia , socofraco , chuteforte, chutemedia, chutefraco, voadoraforte, voadoramedia, voadorafraco, especial01 , especial02 , especial03 , especial04 , especial05 , especial06 , especial07, especial08, especial09, especial10):          
        limite = 0  
        # self.game.luta_encerrada
        
        if self.direcao == 10: 
            limite = len(socoforte) - 1      
            if int(self.indice) <= limite:                                            
                self.teclaprecionada = False
                sprt = pg.sprite.Sprite(sprites)        
                sprt.image = socoforte[int(self.indice)]
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h) 

        #Animação        
        if self.esquerda:

            if self.direcao == 0:                     
                
                # aplicar_animacao(self, parado, sprites)
                limite = len(parado) - 1      
                if int(self.indice) > limite:
                    self.indice = limite            
                sprt = pg.sprite.Sprite(sprites)        
                sprt.image = parado[int(self.indice)]
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h) 
            
            if self.direcao == 1:                         
                limite = len(tras) - 1         
                if int(self.indice) > limite:
                    self.indice = limite
                sprt = pg.sprite.Sprite(sprites)      
                sprt.image = tras[int(self.indice)]
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h) 

            if self.direcao == 2:                         
                limite = len(frente) - 1         
                if int(self.indice) > limite:
                    self.indice = limite
                sprt = pg.sprite.Sprite(sprites)         
                sprt.image = frente[int(self.indice)]
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h)        

            if self.direcao == 3:                         
                limite = len(agachado) - 1         
                if int(self.indice) > limite:
                    self.indice = limite
                sprt = pg.sprite.Sprite(sprites)           
                sprt.image = agachado[int(self.indice)]
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h) 

            if self.direcao == 4:                         
                limite = len(pulo) - 1         
                if int(self.indice) > limite:
                    self.indice = limite
                sprt = pg.sprite.Sprite(sprites)       
                sprt.image = pulo[int(self.indice)]
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h) 

            if self.direcao == 5:                         
                limite = len(pulo_tras) - 1         
                if int(self.indice) > limite:
                    self.indice = limite
                sprt = pg.sprite.Sprite(sprites)            
                sprt.image = pulo_tras[int(self.indice)]
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h)

            if self.direcao == 6:                         
                limite = len(pulo_frente) - 1         
                if int(self.indice) > limite:
                    self.indice = limite
                sprt = pg.sprite.Sprite(sprites)              
                sprt.image = pulo_frente[int(self.indice)]
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h)
        else:
            if self.direcao == 0:     
                limite = len(parado) - 1      
                if int(self.indice) > limite:
                    self.indice = limite            
                sprt = pg.sprite.Sprite(sprites)                        
                sprt.image = pg.transform.flip(parado[int(self.indice)], True, False)
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y,5,5) 
            
            if self.direcao == 2:                         
                limite = len(tras) - 1         
                if int(self.indice) > limite:
                    self.indice = limite
                sprt = pg.sprite.Sprite(sprites)      
                sprt.image = pg.transform.flip(tras[int(self.indice)], True, False)
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h) 

            if self.direcao == 1:                         
                limite = len(frente) - 1         
                if int(self.indice) > limite:
                    self.indice = limite
                sprt = pg.sprite.Sprite(sprites)         
                sprt.image = pg.transform.flip(frente[int(self.indice)], True, False)
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h)        

            if self.direcao == 3:                         
                limite = len(agachado) - 1         
                if int(self.indice) > limite:
                    self.indice = limite
                sprt = pg.sprite.Sprite(sprites)           
                sprt.image = pg.transform.flip(agachado[int(self.indice)], True, False)
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h) 

            if self.direcao == 4:                         
                limite = len(pulo) - 1         
                if int(self.indice) > limite:
                    self.indice = limite
                sprt = pg.sprite.Sprite(sprites)       
                sprt.image = pg.transform.flip(pulo[int(self.indice)], True, False)
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h) 

            if self.direcao == 6:                         
                limite = len(pulo_tras) - 1         
                if int(self.indice) > limite:
                    self.indice = limite
                sprt = pg.sprite.Sprite(sprites)            
                sprt.image = pg.transform.flip(pulo_tras[int(self.indice)], True, False)
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h)

            if self.direcao == 5:                         
                limite = len(pulo_frente) - 1         
                if int(self.indice) > limite:
                    self.indice = limite
                sprt = pg.sprite.Sprite(sprites)              
                sprt.image = pg.transform.flip(pulo_frente[int(self.indice)], True, False)
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h)
        

        # agachar e pulo 
        if self.direcao in [3,4]:
            if  self.indice < limite:
                self.indice += 0.1
        # pulo diagonal
        elif self.direcao in [5,6]:
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
    if self.direcao in [1] and dx > 0:
        dx -= self.velocidade_x
     # direita        
    elif self.direcao in [2] and dx < (TELA_LARGURA - self.Bloco.w):
        dx += self.velocidade_x        
    
    #pulo diagonal
    if self.direcao in [5] and dx > 0:
        dx -= self.velocidade_xy
     # direita        
    elif self.direcao in [6] and dx < (TELA_LARGURA - self.Bloco.w):
        dx += self.velocidade_xy

    #pulo reto
    if self.pulo == 1:
        self.gravidade += self.velocidade_y
        dy += int(self.gravidade)
        
        if self.gravidade >= gravidadeY:        
            self.pulo = 0        
            self.direcao = 0
            self.gravidade = (gravidadeY * -1)
            dy = (TELA_ALTURA_CHAO - self.Bloco.h)
               
    self.Bloco.x = dx
    self.Bloco.y = dy