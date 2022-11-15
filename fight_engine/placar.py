import pygame as pg
from settings import *

class Placar:
    def __init__(self, game):
        self.game = game
        self.reverter = 0

    def atualizar(self):
       
    #    CRONOMETRO
        if self.game.Tempo == -99:
            self.game.Tempo = 0
        elif self.game.Tempo > 0 and self.game.Player01.saude > 0 and self.game.Player02.saude > 0:
            self.game.Tempo -= 0.035

        # TESTE TESTE TESTE
        # if self.game.Tempo > 0 and self.game.Player01.saude > 0 and self.game.Player02.saude > 0:
        #     self.reverter += 1
        #     self.game.Player01.saude -= 1
        #     self.game.Player02.saude -= 1

    def desenhar(self):
        barra_largura_padrao = BARRA_ENERGIA
        barra_altura = 50
        barra_x = 13
        barra_y = 15
        cor_tempo = AMARELO      

        barra01 = pg.Rect(barra_x, barra_y, barra_largura_padrao, barra_altura)
        barra_tempo = pg.Rect(barra01.x + barra_largura_padrao + 10, barra_y, barra_largura_padrao, barra_altura)
        barra02 = pg.Rect(barra_tempo.x + 63 , barra_y, barra_largura_padrao, barra_altura)

        energia01 = pg.Rect(barra_x, barra_y, self.reverter, barra_altura)
        energia02 = pg.Rect(barra_tempo.x + 63 , barra_y, self.game.Player02.saude, barra_altura)
        

        fonte_tempo = pg.font.SysFont('arial', 50, True, False)
                
        if int(self.game.Tempo) < 30:
            cor_tempo = VERMELHO
                
        tempo = fonte_tempo.render(f'{int(self.game.Tempo)}', True, cor_tempo)
        
        if int(self.game.Tempo) < 10:
            tempo = fonte_tempo.render(f'0{int(self.game.Tempo)}', True, cor_tempo)

        self.game.Tela.blit(tempo, barra_tempo)
        
        #barra esquerda Player 01
        pg.draw.rect(self.game.Tela, AMARELO, barra01 )
        pg.draw.rect(self.game.Tela, VERMELHO, energia01) 
        pg.draw.rect(self.game.Tela, BRANCO, barra01, 3)
        
        #barra direita Player 02
        pg.draw.rect(self.game.Tela, VERMELHO, barra02)          
        pg.draw.rect(self.game.Tela, AMARELO, energia02) 
        pg.draw.rect(self.game.Tela, BRANCO, barra02, 3) 
