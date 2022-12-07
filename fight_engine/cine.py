import pygame as pg
import os
from settings import *
from essencial import *

# RECUPERAR LISTAS DE IMAGENS POR MOVIMENTOS (FRAME)
def carregar_movimentos(destino, spritesheet,  inverter, lista_origem):
    
    lista_destino = []
    lista_generica = lista_origem

    if inverter:
        lista_generica = lista_origem[::-1]

    for frame in lista_generica:
        # RECUPERA IMAGEM
        imagem = spritesheet.subsurface(frame[0])        
        # RECUPERA O TAMANHO DA IMAGEM
        transformar = (0,0,0,0)
        if len(frame) > 0:
            transformar = frame[1]
        #COLISÕES
        # colisao = ((0,0), (100,100))
        # colisoes = [colisao, colisao, colisao]
        if len(frame) > 2:
            colisao = frame[2] 
            # self.colisoes = colisao
        lista_destino.append([imagem, transformar, colisao])

    if len(lista_destino) > 0:
        destino.append(lista_destino)

def recuperar_frame(selecionado, listaorigem):
    spritesheet = pg.image.load(os.path.join(selecionado.game.Imagens, selecionado.spritesheet))    
    
    retorno = []
    for indice in listaorigem:
        carregar_movimentos(retorno, spritesheet, False,  listaorigem[indice])        

    return retorno

# FIM - RECUPERAR LISTAS DE IMAGENS POR MOVIMENTOS (FRAME)

# EXECUTAR ANIMAÇÕES E COLISÕES
def executar_animacao(self, sprites):

    if len(self.personagem) > 0:
        
        limite = 0  

        sprt = pg.sprite.Sprite(sprites)
        transform = ((0,0),(0,0))
        
        def calcular_limite(lista):
            lmt = len(lista) - 1      
            if int(self.indice) > lmt:
                self.indice = lmt
            return lmt
            

        def retorno_imagem(esquerda, posicao_imagem):            
            imagemLocal = posicao_imagem[0]
            imagemLocal = pg.transform.scale(imagemLocal, (sprt.rect.w, sprt.rect.h))

            if esquerda == False:
                imagemLocal = pg.transform.flip(imagemLocal, True, False)                
            return imagemLocal


        def colisoes(self, oponente, lista_colisoes):
            retorno = False
            indice_colisao = 0
            self.colisoes = []
            
            for bloco_colisao in lista_colisoes[2]:
                bc = pg.Rect(bloco_colisao[0], bloco_colisao[1], bloco_colisao[2], bloco_colisao[3]) 
                bc.center = self.BlocoMov.center
                # bc.bottom = self.BlocoMov.bottom #- (bc.h * indice_colisao)
                
                if self.esquerda:
                    bc.left = self.BlocoMov.left + bloco_colisao[0]                    
                    
                else:
                    bc.right = self.BlocoMov.right - bloco_colisao[0]                    
                
                bc.bottom = self.BlocoMov.bottom - bloco_colisao[1]                    

                indice_colisao += 1                

# CALCULO PRINCIPAL DE GOLPES
                if len(bloco_colisao) > 4:

                    # CAIXA DE GOLPE
                    if bloco_colisao[4]:

                        if DEBUG:
                            pg.draw.rect(self.game.superficie, VERDE, bc)

                        for ebloc in oponente.colisoes:   
                            bc2 = pg.Rect(ebloc[0], ebloc[1], ebloc[2], ebloc[3])                         
                            if pg.Rect.colliderect(bc, bc2):
                                
                                oponente.golpe = 0
                                # oponente.indice = 0
                                oponente_saude = 0

                                if len(ebloc) >= 5:
                                    oponente_saude = ebloc[5]

                                if oponente.movimento in [4, 5, 6]:
                                    oponente.movimento = 14
                                elif self.movimento in [0, 1, 2] and oponente.movimento in [0, 1, 2]:
                                    oponente.movimento = 15                                
                                elif self.movimento == 3 and oponente.movimento in [0, 1, 2, 3]:
                                    oponente.movimento = 14                                
                                else:
                                    oponente.movimento = 15
    
                                if DEBUG:
                                    pg.draw.rect(self.game.superficie, VERMELHO, bc2)


                                oponente.saude = (oponente.saude - (bloco_colisao[5] + oponente_saude) )
                                break
# CALCULO PRINCIPAL DE GOLPES - FIM

                        if DEBUG:
                            pg.draw.rect(self.game.superficie, VERDE, bc)
                    else:
                        self.colisoes.append(bc)
                        if DEBUG:
                            pg.draw.rect(self.game.superficie, PRETO, bc, 2)
                    
                    retorno = bloco_colisao[4]
            return retorno


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
        generico = self.personagem[self.movimento] # PARADO

    # GOLPES
        if self.golpe > 0: 
            generico = self.personagem[self.golpe]

        else:
            # andar esquerda direita
            if self.movimento == 1: 
                generico = esquerda_direita(self.personagem[2], self.personagem[1])

            # andar esquerda direita (Iverter quando estiver na direita)
            if self.movimento == 2: 
                generico = esquerda_direita(self.personagem[1], self.personagem[2])
            
            # pulo diagonal
            if self.movimento == 5: 
                generico = esquerda_direita(self.personagem[6], self.personagem[5])
            
            # pulo diagonal (Iverter quando estiver na direita)
            if self.movimento == 6: 
                generico = esquerda_direita(self.personagem[5], self.personagem[6])



        limite = calcular_limite(generico)

        sprt.rect = retorno_retangulo(self.esquerda, generico[int(self.indice)])
        sprt.image = retorno_imagem(self.esquerda, generico[int(self.indice)])

        oponente = self.game.Player02
        if self.IDP == 'P2':
            oponente = self.game.Player01
        colisoes(self, oponente,  generico[int(self.indice)])

####################################################################
        if self.movimento in [14]:
                if  int(self.indice) <= limite:
                    self.indice += 0.1
                    self.movimento = 14
                    aplicar_movimentacao(self, oponente)
                else:
                    self.movimento = 0
                    self.indice = 0
        if self.movimento in [15]:
                if  int(self.indice) <= limite:
                    self.indice += 0.1
                    self.movimento = 15
                    aplicar_movimentacao(self, oponente)
                else:
                    self.movimento = 0
                    self.indice = 0
        # agachar 
        elif self.movimento in [3]:
            if  self.indice < limite:
                self.indice += 1
            else:
                self.golpe = 0

        # pulo 
        elif self.movimento in [4,5,6]:

            if self.indice > 0 and self.BlocoMov.bottom == self.game.chao:
                self.movimento = 0
                self.golpe = 0
                self.indice = 0
            elif  self.indice < limite:
                self.indice += 0.17

# GOLPES
        elif self.golpe > 0:
            if  self.indice < limite:
                self.indice += 0.5
            else:
                self.indice = 0
                self.movimento = 0
                self.golpe = 0
        else:
            if  self.indice > limite:
                self.indice = 0
            else:
                self.indice += 0.1