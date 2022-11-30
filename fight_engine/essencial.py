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


# LISTAS DE IMAGENS POR MOVIMENTOS
def carregar_movimentos(self, spritesheet,  inverter, lista_origem, numero, lista_destino):
    
    if len(self.personagem) > numero:

        lista_generica = lista_origem[numero]

        if inverter:
            lista_generica = lista_origem[numero][::-1]

        for frame in lista_generica:
            # RECUPERA IMAGEM
            imagem = spritesheet.subsurface(frame[0])        

            # RECUPERA O TAMANHO DA IMAGEM
            transform = (0,0,0,0)
            if len(frame) > 0:
                transform = frame[1]

            #COLISÕES
            # colisao = ((0,0), (100,100))
            # colisoes = [colisao, colisao, colisao]
            if len(frame) > 2:
                colisao = frame[2] 
                # self.colisoes = colisao

            lista_destino.append([imagem, transform, colisao])

def animacao_comportamento(self, spritesheet, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, socoforte , socoagachado, chuteforte, chuteagachado, voadoradiagonal, atingidoDePeRosto):
   
# RECUPERAR TODAS AS IMAGENS
    spritesheet = pg.image.load(os.path.join(self.game.Imagens, self.spritesheet))    
    
    # for numero in self.personagem:
    #     carregar_movimentos(self, spritesheet, False,  self.personagem, numero, parado)

# PARADO
    carregar_movimentos(self, spritesheet, False,  self.personagem, 0, parado)    
# FRENTE
    carregar_movimentos(self, spritesheet, False,  self.personagem, 1, frente)    
# TRAS
    carregar_movimentos(self, spritesheet, False,  self.personagem, 2, tras)    
# AGACHADO
    carregar_movimentos(self, spritesheet, False,  self.personagem, 3, agachado)    
# PULO RETO
    carregar_movimentos(self, spritesheet, False,  self.personagem, 4, pulo)    
# PULO FRENTE
    carregar_movimentos(self, spritesheet, False,  self.personagem, 5, pulo_frente)
# PULO TRAS
    carregar_movimentos(self, spritesheet, True,  self.personagem, 6, pulo_tras)    

# SOCO FORTE
    carregar_movimentos(self, spritesheet, False,  self.personagem, 7, socoforte)
# SOCO AGACHADO
    carregar_movimentos(self, spritesheet, False,  self.personagem, 8, socoagachado)
# CHUTE FORTE
    carregar_movimentos(self, spritesheet, False,  self.personagem, 9, chuteforte)
# CHUTE AGACHADO
    carregar_movimentos(self, spritesheet, False,  self.personagem, 10, chuteagachado)
# CHUTE VOADORA
    carregar_movimentos(self, spritesheet, False,  self.personagem, 11, voadoradiagonal)
    
# CHUTE VOADORA
    carregar_movimentos(self, spritesheet, False,  self.personagem, 12, atingidoDePeRosto)
# VITORIA
    # carregar_movimentos(self, spritesheet, False,  self.personagem[6], vitoria)

# APLICAR ANIMAÇÕES
def animacao(self, sprites, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, socoforte , socoagachado, chuteforte, chuteagachado, voadoradiagonal, atingidoDePeRosto):
        
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

                    # É UMA CAIXA GOLPE
                    if bloco_colisao[4]:

                        if DEBUG:
                            pg.draw.rect(self.game.superficie, VERDE, bc)

                        for ebloc in oponente.colisoes:   
                            bc2 = pg.Rect(ebloc[0], ebloc[1], ebloc[2], ebloc[3])                         
                            if pg.Rect.colliderect(bc, bc2):
                                oponente.movimento = 100
                                # oponente.indice = 0
                                oponente_saude = 0

                                if len(ebloc) > 5:
                                    oponente_saude = ebloc[5]
                                    
                                if DEBUG:
                                    pg.draw.rect(self.game.superficie, VERMELHO, bc2)

                                oponente.saude = (oponente.saude - (bloco_colisao[5] + oponente_saude) )
# CALCULO PRINCIPAL DE GOLPES - FIM

                        if DEBUG:
                            pg.draw.rect(self.game.superficie, VERDE, bc)
                    else:
                        self.colisoes.append(bc)
                        if DEBUG:
                            pg.draw.rect(self.game.superficie, PRETO, bc, 2)
                                        
                    # if len(bloco_colisao) > 5:
                    #     CALCULAR DANO
                    

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

        if self.movimento == 12:
            generico = chuteforte
        
        if self.movimento == 13:
            generico = chuteagachado

        if self.movimento == 14:
            generico = voadoradiagonal
        
        if self.movimento == 100:
            generico = atingidoDePeRosto

        limite = calcular_limite(generico)
            
        oponente = self.game.Player02

        if self.IDP == 'P2':
            oponente = self.game.Player01

        sprt.rect = retorno_retangulo(self.esquerda, generico[int(self.indice)])
        sprt.image = retorno_imagem(self.esquerda, generico[int(self.indice)])

        colisoes(self, oponente,  generico[int(self.indice)])
        

####################################################################
        if self.movimento in [100]:
                if  int(self.indice) < limite:
                    self.indice += 0.5
                    self.movimento = 100
                    aplicar_movimentacao(self.game.Player02, self.game.Player02.gravidade, self.game.Player01)
                else:
                    self.movimento = 0
        elif self.golpe:
            if  self.indice < limite:
                self.indice += 0.5
            elif self.movimento in [11] :
                # self.indice = 0
                # self.movimento = 0
                self.golpe = False
            elif self.movimento in [14]:
                if  self.indice < limite:
                    self.indice += 0.17
            else:
                self.indice = 0
                self.movimento = 0
                self.golpe = False
        # agachar 
        elif self.movimento in [3]:
            if  self.indice < limite:
                self.indice += 1
        # pulo 
        elif self.movimento in [4,5,6, 11]:
            if  self.indice < limite:
                self.indice += 0.17
        # pulo diagonal
        # elif self.movimento in [5,6]:
        #     if  self.indice < limite:
        #         self.indice += 0.15
        # direta esquerda
        else:
            if  self.indice > limite:
                self.indice = 0
            else:
                self.indice += 0.1
        
# APLICAR MOVIMENTAÇÃO        
def aplicar_movimentacao(self, gravidadeY, oponente):
    global dx
    global dy
    dx = self.BlocoMov.x
    dy = self.BlocoMov.y

    # colide = pg.Rect.colliderect(self.BlocoMov, oponente.BlocoMov)

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
    if self.pulo:
        if self.movimento in [5] and dx > 0:
            if colisao_esquerda == False:
                dx -= self.velocidade_xy
        # direita        
        elif self.movimento in [6] and dx < (TELA_LARGURA - self.BlocoMov.w):
            if colisao_direita == False:
                dx += self.velocidade_xy
        elif self.golpe or self.movimento in [5,6]:
            if self.esquerda:
                dx += self.velocidade_xy
            else:
                dx -= self.velocidade_xy

    #pulo reto
    if self.pulo == 1:
        self.gravidade += self.velocidade_y
        dy += int(self.gravidade)
        
        if self.gravidade >= gravidadeY:        
            self.pulo = 0        
            self.movimento = 0
            self.gravidade = (gravidadeY * -1)
            dy = (self.game.chao - self.BlocoMov.h)
               
    if self.movimento in [100] and dx > 0:        
        if self.esquerda:
            dx -= self.velocidade_x
        elif dx < (TELA_LARGURA - self.BlocoMov.w):
            dx += self.velocidade_x

    self.BlocoMov.x = dx
    self.BlocoMov.y = dy

    colisao_esquerda = False
    colisao_direita = False
    
# RECUPERAR ENTRADA DE COMANDOS
def monitorar_teclas_movimento(self, evg):
    
    pressionando = pg.key.get_pressed()
    tecla = 0

    oponente = self.game.Player02
        
    if self.IDP == 'P2':
        oponente = self.game.Player01

    if self.game.luta_encerrada:
        self.movimento = 0

    elif evg.type == pg.KEYDOWN or True in pressionando:

        if evg.type == pg.KEYDOWN:
            tecla = evg.key

        if self.game.luta_encerrada == False:
            # if tecla == self.tecla_soco :                
            # if tecla == self.tecla_chute:
            if tecla == self.tecla_soco and self.movimento in [0,1,2]:
                self.movimento = 10
                self.golpe = True
                self.indice = 0
            if tecla == self.tecla_soco and self.movimento in [3]:
                self.movimento = 11
                self.golpe = True
                self.indice = 0
            if tecla == self.tecla_soco and self.movimento in [4,5,6]:
                self.movimento = 11
                self.golpe = True
                self.indice = 0
            if tecla == self.tecla_chute and self.movimento in [0,1,2] :
                self.movimento = 12
                self.golpe = True
                self.indice = 0
            if tecla == self.tecla_chute and self.movimento in [3] :
                self.movimento = 13
                self.golpe = True
                self.indice = 0
            if tecla == self.tecla_chute and self.movimento in [5,6]:
                self.movimento = 14
                self.golpe = True
                self.indice = 0

        if self.golpe == False:
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
    
    elif evg.type == pg.KEYUP and self.pulo == 0 and self.golpe == False:
        self.movimento = 0
        self.indice = 0
