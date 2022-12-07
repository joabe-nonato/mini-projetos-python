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
socoforte  = []
socoagachado = []
chuteforte = []
chuteagachado = []
voadoradiagonal = []
atingidoDePeRosto = []
voadoravertical = []
socoaereo = []
atingidoQueda = []

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
        self.colisoes = []
        self.pulo = 0        
        self.golpe = False 
        self.esquerda = False
        self.limite_esquerdo = False
        self.limite_direito = False        
        self.saude = BARRA_ENERGIA            
        self.movimento = 0 #0 = parado, 1 = esquerda, 2 = direita, 3 = agacha, 4 = pulo

        self.BlocoMov = pg.Rect(alinhar_centro(datap[selecionado].largura, TELA_CENTRO_V, self.esquerda), self.game.chao, BLOCOMOV_LARGURA, BLOCOMOV_ALTURA)
        self.BlocoMov.bottom = self.game.chao
        self.tecla_esquerda = pg.K_LEFT
        self.tecla_cima = pg.K_UP
        self.tecla_direita = pg.K_RIGHT
        self.tecla_baixo = pg.K_DOWN
        self.tecla_soco = pg.K_m
        self.tecla_chute = pg.K_n

        global gravidadeY
        gravidadeY = gravidade[selecionado]

        animacao_comportamento(self, spritesheet, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, socoforte , socoagachado, chuteforte, chuteagachado, voadoradiagonal, atingidoDePeRosto, voadoravertical, socoaereo, atingidoQueda)

    def monitorar_golpes(self, evg):
        monitorar_golpes(self, evg)

    def monitorar_movimentos(self):
        monitorar_movimentos(self)

    def atualizar(self):
        self.esquerda = (self.BlocoMov.x < self.game.Player01.BlocoMov.x)
        aplicar_movimentacao(self, gravidadeY, self.game.Player01)        

    def desenhar(self):
        
        redenderizar(self,'Blue')

        # executar animações
        sprites = pg.sprite.Group()  
        animacao(self, sprites, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, socoforte , socoagachado, chuteforte, chuteagachado, voadoradiagonal, atingidoDePeRosto, voadoravertical, socoaereo, atingidoQueda)
        sprites.draw(self.game.superficie)
        
        informacoes(self.game,'Red', f'P2 e:{self.esquerda} x:{self.BlocoMov.x} y:{self.BlocoMov.y} w:{self.BlocoMov.w} d:{self.movimento} g:{self.gravidade}', (TELA_LARGURA // 2) + 20, 200)
        

    