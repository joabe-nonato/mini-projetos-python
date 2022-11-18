from tkinter import Y
import pygame as pg
from settings import *

class Placar:
    def __init__(self, game):
        self.game = game
        self.reverter = 0
        self.velocidade = 1

    def atualizar(self):
       
    #    CRONOMETRO
        if self.game.Tempo == -99:
            self.game.Tempo = 0
        elif self.game.Tempo > 0 and self.game.Player01.saude > 0 and self.game.Player02.saude > 0:
            self.game.Tempo -= 0.035

        # TESTE TESTE TESTE        
        if self.game.Tempo > 0 and self.game.Player01.saude > 0 and self.game.Player02.saude > 0:
            self.reverter += int(self.velocidade)
            self.game.Player01.saude -= int(self.velocidade)
            self.game.Player02.saude -= int(self.velocidade)

    def desenhar(self):

        def alinhar_centro(largura):
            return ((TELA_LARGURA - largura) / 2)

        fonte_tempo = pg.font.SysFont('arial', 53, True, False)
        barra_largura_padrao = BARRA_ENERGIA
        barra_altura = 40        
        barra_y = 40
        margem_lateral = 5
        barra_x = (margem_lateral + 2)
        
        cor_tempo = AZUL      
        
        barra02 = pg.Rect(63 , barra_y, barra_largura_padrao, barra_altura)        
        # energia02 = pg.Rect(barra_tempo.x + 63 , barra_y, self.game.Player02.saude, barra_altura)
        
## BACKGROUND BARRA        
        branca_largura = (TELA_LARGURA - (margem_lateral * 2))        
        branca = pg.Rect(alinhar_centro(branca_largura), barra_y, branca_largura , barra_altura)   
        pg.draw.rect(self.game.Tela, AMARELO, (branca)) 
        
# #barra esquerda Player 01
        barra01 = pg.Rect(barra_x, barra_y + 2, barra_largura_padrao, barra_altura - 4)
        energia01 = pg.Rect(barra_x, barra_y + 2, self.reverter, barra_altura - 4)

        pg.draw.rect(self.game.Tela, AMARELO, barra01 )
        pg.draw.rect(self.game.Tela, VERMELHO, energia01) 
        # pg.draw.rect(self.game.Tela, BRANCO, barra01, 3)
        
        
# #barra direita Player 02
        # pg.draw.rect(self.game.Tela, VERMELHO, barra02)          
        # pg.draw.rect(self.game.Tela, AMARELO, energia02) 
        # pg.draw.rect(self.game.Tela, BRANCO, barra02, 3) 

## CRONOMETRO
        if int(self.game.Tempo) < 30 or self.reverter > 300:
            cor_tempo = VERMELHO
                
        tempo = fonte_tempo.render(f'{ int(self.game.Tempo) }', True, cor_tempo)
        tempo_sombra = fonte_tempo.render(f'{ int(self.game.Tempo) }', True, PRETO)
        
        # ADICIONAR CASA A ESQUERDA
        if int(self.game.Tempo) < 10:
            tempo = fonte_tempo.render(f'0{int(self.game.Tempo)}', True, cor_tempo)

        barra_tempo = pg.Rect(alinhar_centro(60), branca.y + barra_altura - 3, 60, barra_altura)        
        barra_tempo_combra = pg.Rect(alinhar_centro(60) + 2, branca.y + barra_altura, 60, barra_altura)
        self.game.Tela.blit(tempo_sombra, barra_tempo_combra)
        self.game.Tela.blit(tempo, barra_tempo)        

        if DEBUG:
            pg.draw.line(self.game.Tela, 'White', (TELA_CENTRO_HORIZONTAL, 0), (TELA_CENTRO_HORIZONTAL, TELA_ALTURA), 3)
