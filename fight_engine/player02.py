import pygame as pg
from essencial import *
from settings import *
from data import *

selecionado = 1

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
socoagachado = []                           
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
        self.IDP = 'P2'            
        self.indice = 0          
        self.personagem = personagem[selecionado]
        self.spritesheet = spritesheet[selecionado]
        self.gravidade = (gravidade[selecionado] * -1)                                
        self.velocidade_x = velocidade_x[selecionado]
        self.velocidade_y = velocidade_y[selecionado]
        self.velocidade_xy = velocidade_xy[selecionado]
        self.teclaprecionada = False
        # self.colisao_direita  = False
        # self.colisao_esquerda = False
        self.pulo = 0        
        self.golpe = False 
        self.bloco_golpe = pg.Rect(0,0,0,0)
        self.esquerda = False
        self.limite_esquerdo = False
        self.limite_direito = False        
        self.saude = BARRA_ENERGIA            
        self.movimento = 0 #0 = parado, 1 = esquerda, 2 = direita, 3 = agacha, 4 = pulo

        self.BlocoMov = pg.Rect(alinhar_centro(datap[selecionado].largura, TELA_CENTRO_V, self.esquerda), self.game.chao, 200, 250)
        self.BlocoMov.bottom = self.game.chao
        self.tecla_esquerda = pg.K_LEFT
        self.tecla_cima = pg.K_UP
        self.tecla_direita = pg.K_RIGHT
        self.tecla_baixo = pg.K_DOWN
        self.tecla_soco = pg.K_m

        global gravidadeY
        gravidadeY = gravidade[selecionado]

        animacao_comportamento(self, spritesheet, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, vitoria, derrota, socoforte, socoagachado , socomedia , socofraco , chuteforte, chutemedia, chutefraco, voadoraforte, voadoramedia, voadorafraco, especial01 , especial02 , especial03 , especial04 , especial05 , especial06 , especial07, especial08, especial09, especial10)

    def Golpe(self, tecla):
            if tecla == self.tecla_soco and self.movimento in [0,1,2] :
                self.movimento = 10
                self.golpe = True
                self.indice = 0
            if tecla == self.tecla_soco and self.movimento in [3] :
                self.movimento = 11
                self.golpe = True
                self.indice = 0

    def eventos(self):                
        if self.game.Tempo > 0 and self.saude > 0 or TEMPO_LUTA == -99:
            monitorar_teclas_movimento(self, self.game.Player01)           
        else:
            self.movimento = 0

    def atualizar(self):
        self.esquerda = (self.BlocoMov.x < self.game.Player01.BlocoMov.x)
        aplicar_movimentacao(self, gravidadeY, self.game.Player01)        

    def desenhar(self):
        
        redenderizar(self,'Blue')

        # executar animações
        sprites = pg.sprite.Group()  
        animacao(self, sprites, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, vitoria, derrota, socoforte, socoagachado , socomedia , socofraco , chuteforte, chutemedia, chutefraco, voadoraforte, voadoramedia, voadorafraco, especial01 , especial02 , especial03 , especial04 , especial05 , especial06 , especial07, especial08, especial09, especial10)
        sprites.draw(self.game.superficie)
        

        informacoes(self.game,'Red', f'P2 e:{self.esquerda} x:{self.BlocoMov.x} y:{self.BlocoMov.y} w:{self.BlocoMov.w} d:{self.movimento} g:{self.gravidade}', (TELA_LARGURA // 2), 100)
        

    