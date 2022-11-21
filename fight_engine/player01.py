import pygame as pg
from essencial import *
from settings import *
from data import *

selecionado = 0

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

class Player01:
    def __init__(self, game) -> None:
        self.game = game        
        self.indice = 0                  
        self.Bloco = pg.Rect(alinhar_centro(datap[selecionado].largura, TELA_CENTRO_V), TELA_ALTURA_CHAO - datap[selecionado].altura, datap[selecionado].largura, datap[selecionado].altura)
        self.personagem = personagem[selecionado]
        self.spritesheet = spritesheet[selecionado]                
        self.gravidade = (gravidade[selecionado] * -1)                
        self.velocidade_x = velocidade_x[selecionado]
        self.velocidade_y = velocidade_y[selecionado]
        self.velocidade_xy = velocidade_xy[selecionado]
        self.teclaprecionada = False
        self.pulo = 0       
        self.golpe = False 
        self.bloco_golpe = pg.Rect(0,0,0,0)
        self.esquerda = True
        self.saude = BARRA_ENERGIA            
        self.movimento = 0 #0 = parado, 1 = esquerda, 2 = direita, 3 = agacha, 4 = pulo

        self.tecla_esquerda = pg.K_a
        self.tecla_cima = pg.K_w
        self.tecla_direita = pg.K_d
        self.tecla_baixo = pg.K_s
        
        global gravidadeY
        gravidadeY = gravidade[selecionado]

        animacao_comportamento(self, spritesheet, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, vitoria, derrota, socoforte, socoagachado , socomedia , socofraco , chuteforte, chutemedia, chutefraco, voadoraforte, voadoramedia, voadorafraco, especial01 , especial02 , especial03 , especial04 , especial05 , especial06 , especial07, especial08, especial09, especial10)

    def Golpe(self, tecla):
            if tecla == pg.K_p and self.movimento in [0,1,2] :
                self.movimento = 10
                self.golpe = True
                self.indice = 0
            if tecla == pg.K_p and self.movimento in [3] :
                self.movimento = 11
                self.golpe = True
                self.indice = 0

    def eventos(self):
        self.esquerda = (self.Bloco.x < self.game.Player02.Bloco.x)
        
        if self.game.Tempo > 0 and self.saude > 0 or TEMPO_LUTA == -99:
            monitorar_teclas_movimento(self, self.game.Player02)           
        else:
            self.movimento = 0

    def atualizar(self):
        aplicar_movimentacao(self, gravidadeY)        

    def desenhar(self):
        
        redenderizar(self,'Blue')

        # executar animações
        sprites = pg.sprite.Group()  
        animacao(self, sprites, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, vitoria, derrota, socoforte, socoagachado , socomedia , socofraco , chuteforte, chutemedia, chutefraco, voadoraforte, voadoramedia, voadorafraco, especial01 , especial02 , especial03 , especial04 , especial05 , especial06 , especial07, especial08, especial09, especial10)
        sprites.draw(self.game.Tela)
        
        informacoes(self.game,'Blue', f'P1 e:{self.esquerda} x:{self.Bloco.x} y:{self.Bloco.y} w:{self.Bloco.w} h:{self.Bloco.h} d:{self.movimento} g:{self.gravidade}', 10, 100)            

        
