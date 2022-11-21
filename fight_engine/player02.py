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
        self.indice = 0             
        self.Bloco = pg.Rect(alinhar_centro(datap[selecionado].largura, TELA_CENTRO_V, False), TELA_ALTURA_CHAO - datap[selecionado].altura, datap[selecionado].largura, datap[selecionado].altura)
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
        self.limite_esquerdo = False
        self.limite_direito = False        
        self.saude = BARRA_ENERGIA            
        self.movimento = 0 #0 = parado, 1 = esquerda, 2 = direita, 3 = agacha, 4 = pulo

        self.tecla_esquerda = pg.K_LEFT
        self.tecla_cima = pg.K_UP
        self.tecla_direita = pg.K_RIGHT
        self.tecla_baixo = pg.K_DOWN

        global gravidadeY
        gravidadeY = gravidade[selecionado]

        animacao_comportamento(self, spritesheet, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, vitoria, derrota, socoforte, socoagachado , socomedia , socofraco , chuteforte, chutemedia, chutefraco, voadoraforte, voadoramedia, voadorafraco, especial01 , especial02 , especial03 , especial04 , especial05 , especial06 , especial07, especial08, especial09, especial10)

    def Golpe(self, tecla):
            if tecla == pg.K_m:
                self.movimento = 10
                self.golpe = True


    def eventos(self):        
        self.esquerda = (self.Bloco.x < self.game.Player01.Bloco.x)
              
        if self.game.Tempo > 0 and self.saude > 0 or TEMPO_LUTA == -99:
            monitorar_teclas_movimento(self, self.game.Player01)           
        else:
            self.movimento = 0  


    def atualizar(self):
        aplicar_movimentacao(self, gravidadeY)        
        

    def desenhar(self):  
        # executar animações
        sprites = pg.sprite.Group()  
        animacao(self, sprites, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, vitoria, derrota, socoforte, socoagachado , socomedia , socofraco , chuteforte, chutemedia, chutefraco, voadoraforte, voadoramedia, voadorafraco, especial01 , especial02 , especial03 , especial04 , especial05 , especial06 , especial07, especial08, especial09, especial10)
        sprites.draw(self.game.Tela)

        redenderizar(self,'Red')

        informacoes(self.game,'Red', f'P2 e:{self.esquerda} x:{self.Bloco.x} y:{self.Bloco.y} w:{self.Bloco.w} d:{self.movimento} g:{self.gravidade}', (TELA_LARGURA // 2), 100)
        
        # self.game.Tela.blit(self.sprites, self.Bloco)