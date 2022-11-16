import pygame as pg
import os
from settings import *


def redenderizar(t, cor, objt):
    if DEBUG:
        pg.draw.rect(t, cor, objt, 2)

def criarobjeto(posx, posy, larg, alt, velx = 1, vely = 1):
    return [pg.Rect(posx, posy, larg, alt), [velx, vely]]

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
        imagem = spritesheet.subsurface(posicao)
        imagem = pg.transform.scale(imagem, (self.Bloco.w, self.Bloco.h))
        lista_destino.append(imagem)

def animacao_comportamento(self, spritesheet, parado, frente, tras, agachado, pulo, pulo_diagonal, vitoria, derrota, socoforte , socomedia , socofraco , chuteforte, chutemedia, chutefraco, voadoraforte, voadoramedia, voadorafraco, especial01 , especial02 , especial03 , especial04 , especial05 , especial06 , especial07, especial08, especial09, especial10):
    
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
    carregar_movimentos(self, spritesheet, self.personagem[6], pulo_diagonal)
# PULO TRAS
    # carregar_movimentos(self, spritesheet, self.personagem[6], pulo_tras)    
# VITORIA
    carregar_movimentos(self, spritesheet, self.personagem[7], vitoria)

# EXECUTAR ANIMAÇÕES
def animacao(self, sprites, parado, frente, tras, agachado, pulo, pulo_diagonal, vitoria, derrota, socoforte , socomedia , socofraco , chuteforte, chutemedia, chutefraco, voadoraforte, voadoramedia, voadorafraco, especial01 , especial02 , especial03 , especial04 , especial05 , especial06 , especial07, especial08, especial09, especial10):          
        limite = 0  
        #Animação        
        if self.esquerda:
            if self.direcao == 0:     
                limite = len(parado) - 1      
                if int(self.indice) > limite:
                    self.indice = limite            
                sprt = pg.sprite.Sprite(sprites)        
                sprt.image = parado[int(self.indice)]
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y,5,5) 
            
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

            if self.direcao in [5,6]:                         
                limite = len(pulo_diagonal) - 1         
                if int(self.indice) > limite:
                    self.indice = limite
                sprt = pg.sprite.Sprite(sprites)            
                sprt.image = pulo_diagonal[int(self.indice)]
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h)

            # if self.direcao == 6:                         
            #     limite = len(pulo_frente) - 1         
            #     if int(self.indice) > limite:
            #         self.indice = limite
            #     sprt = pg.sprite.Sprite(sprites)              
            #     sprt.image = pulo_frente[int(self.indice)]
            #     sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h)
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

            if self.direcao in [5,6]:                         
                limite = len(pulo_diagonal) - 1         
                if int(self.indice) > limite:
                    self.indice = limite
                sprt = pg.sprite.Sprite(sprites)            
                sprt.image = pg.transform.flip(pulo_diagonal[int(self.indice)], True, False)
                sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h)

            # if self.direcao == 5:                         
            #     limite = len(pulo_frente) - 1         
            #     if int(self.indice) > limite:
            #         self.indice = limite
            #     sprt = pg.sprite.Sprite(sprites)              
            #     sprt.image = pg.transform.flip(pulo_frente[int(self.indice)], True, False)
            #     sprt.rect = pg.Rect(self.Bloco.x,self.Bloco.y, self.Bloco.w ,self.Bloco.h)
        

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
        