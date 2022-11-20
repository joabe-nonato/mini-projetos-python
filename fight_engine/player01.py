import pygame as pg
from essencial import *
from settings import *
from data import *

selecionado = 0
personagem_altura_chao = (TELA_ALTURA_CHAO - 290)

spritesheet = ''
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
        self.gravidade = (gravidade[selecionado] * -1)                
        self.velocidade_x = velocidade_x[selecionado]
        self.velocidade_y = velocidade_y[selecionado]
        self.velocidade_xy = velocidade_xy[selecionado]
        self.teclaprecionada = False
        self.pulo = 0        
        self.esquerda = True
        self.saude = BARRA_ENERGIA            
        self.direcao = 0 #0 = parado, 1 = esquerda, 2 = direita, 3 = agacha, 4 = pulo
        
        global gravidadeY
        gravidadeY = gravidade[selecionado]

        animacao_comportamento(self, spritesheet, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, vitoria, derrota, socoforte , socomedia , socofraco , chuteforte, chutemedia, chutefraco, voadoraforte, voadoramedia, voadorafraco, especial01 , especial02 , especial03 , especial04 , especial05 , especial06 , especial07, especial08, especial09, especial10)

    def golpe(self, tecla):        

        if self.teclaprecionada:            
            if tecla[pg.K_KP1]:
                self.direcao = 10
            
            if self.teclaprecionada == False:
                self.direcao = 0

        #     if golpe.type == pg.K_KP1:
        #         print('OK')

        # if self.direcao < 10:
        #     tecla = pg.key.get_pressed()        
        #     # SOCO FORTE
        #     if tecla[pg.K_KP1]:
        #         self.direcao = 10

    def eventos(self):
        self.esquerda = (self.Bloco.x < self.game.Player02.Bloco.x)
        self.limite_direito = False
        self.limite_esquerdo = False

        # print(pg.key.stop_text_input(), pg.key.start_text_input())

        if self.game.Tempo > 0 and self.saude > 0 or TEMPO_LUTA == -99:
            tecla = pg.key.get_pressed()

            # Diagonal esquerda
            if tecla[pg.K_w] and self.pulo == 0 and tecla[pg.K_a]:                
                self.pulo = 1
                self.direcao = 5     
                if self.Bloco.y == personagem_altura_chao:  
                    self.indice = 0         
            # Diagonal Direita
            elif tecla[pg.K_w] and self.pulo == 0 and tecla[pg.K_d]:
                self.pulo = 1
                self.direcao = 6
                if self.Bloco.y == personagem_altura_chao:  
                    self.indice = 0
                    
            if self.pulo == 0:  

                # Esquerda
                if tecla[pg.K_a]:                            
                    self.direcao = 1

                    #colisão esquerda
                    if self.esquerda == False and self.game.Player02.pulo == 0:
                        if self.Bloco.x <= (self.game.Player02.Bloco.x + self.game.Player02.Bloco.w):
                            self.direcao = 0
                            self.limite_esquerdo = True

                # Direita
                elif tecla[pg.K_d]:                     
                    self.direcao = 2

                    #colisão direita
                    if self.esquerda and self.game.Player02.pulo == 0:
                        if (self.Bloco.x + self.Bloco.w) >= self.game.Player02.Bloco.x:
                            self.direcao = 0
                            self.limite_direito = True                            
                else:
                    self.direcao = 0
                
                # Pulo
                if tecla[pg.K_w] :                    
                    self.pulo = 1                    
                    self.direcao = 4
                    self.indice = 0
                # Agacha
                elif tecla[pg.K_s] :
                    self.direcao = 3         
            
            self.golpe(tecla)   

        else:
            self.game.luta_encerrada = True
            self.direcao = 0

    def atualizar(self):
        aplicar_movimentacao(self, gravidadeY)        

    def desenhar(self):
        
        # executar animações
        sprites = pg.sprite.Group()  
        animacao(self, sprites, parado, frente, tras, agachado, pulo, pulo_frente, pulo_tras, vitoria, derrota, socoforte , socomedia , socofraco , chuteforte, chutemedia, chutefraco, voadoraforte, voadoramedia, voadorafraco, especial01 , especial02 , especial03 , especial04 , especial05 , especial06 , especial07, especial08, especial09, especial10)
        sprites.draw(self.game.Tela)

        # imagemteste = pg.image.load(os.path.join(self.game.Imagens, "teste.png")).convert_alpha()
        # self.game.Tela.blit(pg.transform.scale(imagemteste, (self.Bloco.w + 60, self.Bloco.h + 60)), (self.Bloco.x - 60, self.Bloco.y - 60))

        redenderizar(self.game.Tela,'Blue', self.Bloco)
        informacoes(self.game,'Blue', f'P1 e:{self.esquerda} x:{self.Bloco.x} y:{self.Bloco.y} w:{self.Bloco.w} d:{self.direcao} g:{self.gravidade}', 10, 100)            
