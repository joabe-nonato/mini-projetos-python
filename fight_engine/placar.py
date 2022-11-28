import pygame as pg
from essencial import *

class Placar:
    def __init__(self, game):
        self.game = game
        self.reverter = 0
        self.velocidade = 1
        self.barra_largura_padrao = BARRA_ENERGIA
        self.barra_altura = 40        
        self.barra_y = 40

    def atualizar(self):
       
    #    CRONOMETRO
        if self.game.Tempo == -99:
            self.game.Tempo = 0
        elif self.game.Tempo > 0 and self.game.Player01.saude > 0 and self.game.Player02.saude > 0:
            self.game.Tempo -= 0.035

        # # TESTE TESTE TESTE        
        if self.game.Tempo > 0 and self.game.Player01.saude > 0 and self.game.Player02.saude > 0:
            self.reverter += int(self.velocidade)
            self.game.Player01.saude -= int(self.velocidade)
            self.game.Player02.saude -= int(self.velocidade)

    def barra_energia(self, esquerda, saude):
                
        margem_lateral = 5
               
        branca_largura = (TELA_CENTRO_V - (margem_lateral * 2))        
        
        x = TELA_CENTRO_V + margem_lateral + 1
        
        if esquerda:
            x = alinhar_centro(branca_largura, TELA_CENTRO_V) 
        
        bar = pg.Rect(x, self.barra_y, branca_largura, self.barra_altura)
        pg.draw.rect(self.game.superficie, BRANCO, bar, 3) 

        if esquerda:            
            pg.draw.rect(self.game.superficie, AMARELO, (x, bar.y + 3, branca_largura , bar.h - 6))            
            pg.draw.rect(self.game.superficie, VERMELHO, (x, bar.y + 3, self.reverter , bar.h - 6)) 
        else:            
            pg.draw.rect(self.game.superficie, AMARELO, (x, bar.y + 3, branca_largura , bar.h - 6)) 
            pg.draw.rect(self.game.superficie, VERMELHO, (x, bar.y + 3, saude , bar.h - 6))
        

    def desenhar(self):

        self.barra_energia(True, self.game.Player01.saude)
        self.barra_energia(False, self.game.Player02.saude)
        
        cor_tempo = AZUL      
        

## CRONOMETRO
        fonte_tempo = pg.font.SysFont('arial', 53, True, False)

        if int(self.game.Tempo) < 30 or self.reverter > 300:
            cor_tempo = VERMELHO
                
        tempo = fonte_tempo.render(f'{ int(self.game.Tempo) }', True, cor_tempo)
        tempo_sombra = fonte_tempo.render(f'{ int(self.game.Tempo) }', True, PRETO)
        
        # ADICIONAR CASA A ESQUERDA
        if int(self.game.Tempo) < 10:
            tempo = fonte_tempo.render(f'0{int(self.game.Tempo)}', True, cor_tempo)
            tempo_sombra = fonte_tempo.render(f'0{ int(self.game.Tempo) }', True, PRETO)

        barra_tempo = pg.Rect(alinhar_centro(60, TELA_LARGURA ), self.barra_altura + 23, 60, self.barra_altura)        
        barra_tempo_combra = pg.Rect(alinhar_centro(60, TELA_LARGURA) + 2, self.barra_altura + 26, 60, self.barra_altura)
    
        self.game.superficie.blit(tempo_sombra, barra_tempo_combra)
        self.game.superficie.blit(tempo, barra_tempo)        

        # cronometo = pg.sprite.Group()  
        
        # sprt = pg.sprite.Sprite(cronometo)
        # transform = ((0,0),(0,0))
        # sprt.rect = retorno_retangulo(self.esquerda, generico[int(self.indice)])
        # sprt.image = retorno_imagem(self.esquerda, generico[int(self.indice)])        
        # cronometo.draw(self.game.superficie)

        if DEBUG:
            pg.draw.line(self.game.superficie, 'White', (TELA_CENTRO_V, 0), (TELA_CENTRO_V, TELA_ALTURA), 3)
