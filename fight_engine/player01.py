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
socoforte  = []
socoagachado = []
chuteforte = []
chuteagachado = []
voadoradiagonal = []
atingidoDePeRosto = []

class Player01:
    def __init__(self, game) -> None:
        self.game = game        
        self.IDP = 'P1'         
        self.indice = 0         
        self.personagem = personagem[selecionado]
        self.spritesheet = spritesheet[selecionado]                
        self.gravidade = (gravidade[selecionado] * -1)                
        self.velocidade_x = velocidade_x[selecionado]
        self.velocidade_y = velocidade_y[selecionado]
        self.velocidade_xy = velocidade_xy[selecionado]
        self.largura = datap[selecionado].largura
        self.altura = datap[selecionado].altura
        self.teclaprecionada = False
        self.colisoes = []
        self.pulo = 0       
        self.golpe = False 
        self.bloco_golpe = pg.Rect(0,0,0,0)
        self.esquerda = True
        self.saude = BARRA_ENERGIA            
        self.movimento = 0 #0 = parado, 1 = esquerda, 2 = direita, 3 = agacha, 4 = pulo

        self.BlocoMov = pg.Rect(alinhar_centro(datap[selecionado].largura, TELA_CENTRO_V, self.esquerda), self.game.chao, 200, 250)
        self.BlocoMov.bottom = self.game.chao
        self.tecla_esquerda = pg.K_a
        self.tecla_cima = pg.K_w
        self.tecla_direita = pg.K_d
        self.tecla_baixo = pg.K_s
        self.tecla_soco = pg.K_p
        self.tecla_chute = pg.K_k
        
        global gravidadeY
        gravidadeY = gravidade[selecionado]

        animacao_comportamento(self, spritesheet, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, socoforte , socoagachado, chuteforte, chuteagachado, voadoradiagonal, atingidoDePeRosto)

    def Golpe(self, tecla):
            if tecla == self.tecla_soco and self.movimento in [0,1,2] :
                self.movimento = 10
                self.golpe = True
                self.indice = 0
            if tecla == self.tecla_soco and self.movimento in [3] :
                self.movimento = 11
                self.golpe = True
                self.indice = 0
            if tecla == self.tecla_soco and self.movimento in [4,5,6] :
                self.movimento = 11
                self.golpe = True
                self.indice = 0
            if tecla == self.tecla_chute and self.movimento in [0,1,2] and self.pulo == False:
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
            # if tecla == self.tecla_chute and self.movimento in [0,1,2] :
            # if tecla == self.tecla_chute and self.movimento in [3] :

    def eventos(self):                
        # if self.game.Tempo > 0 and self.saude > 0 or TEMPO_LUTA == -99:
        #     monitorar_teclas_movimento(self, self.game.Player02)           
        # else:
        #     self.movimento = 0
        if self.game.luta_encerrada:
            self.movimento = 0
        else:
            monitorar_teclas_movimento(self, self.game.Player02)           

    def atualizar(self):
        # self.esquerda = (self.BlocoMov.x < self.game.Player02.BlocoMov.x)
        if self.BlocoMov.bottom == self.game.chao:
            self.esquerda = (self.BlocoMov.x < self.game.Player02.BlocoMov.x)

        aplicar_movimentacao(self, gravidadeY, self.game.Player02)        

    def desenhar(self):
        
        redenderizar(self,'Blue')

        # executar animações
        sprites = pg.sprite.Group()  
        animacao(self, sprites, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, socoforte , socoagachado, chuteforte, chuteagachado, voadoradiagonal, atingidoDePeRosto)
        sprites.draw(self.game.superficie)
        
        informacoes(self.game,'Blue', f'P1 e:{self.esquerda} x:{self.BlocoMov.x} y:{self.BlocoMov.y} w:{self.BlocoMov.w} h:{self.BlocoMov.h} d:{self.movimento} g:{self.gravidade}', 10, 200)            

        
