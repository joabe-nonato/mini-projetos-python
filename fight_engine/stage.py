import pygame as pg
import os
from settings import *

class Estagio:

    def __init__(self, game) -> None:
        self.game = game
        self.hx = ((TELA_LARGURA // 2) * -1)
        
    def fundo(self):        
        dirimage = os.path.join(self.game.Imagens, "fundo.png")
        bckgrd = pg.image.load(dirimage)
        eixoX = (-400 - (self.game.Player01.Bloco.x * (0.2)))        

        eixoY = 10

        # if self.game.Player01.pulo == 1:
        #     eixoY += 10
        # elif self.game.Player01.pulo == 0:
        #     eixoY = 10

        self.game.Tela.blit(pg.transform.scale(bckgrd, (TELA_LARGURA * 2, TELA_ALTURA - 90)), (eixoX, eixoY))



    def chao(self):
        chao = pg.image.load(os.path.join(self.game.Imagens, "chao.png"))
        
        eixoY = 150
        eixoX = ((TELA_LARGURA // 2) * -1)

        # CHAO DIREITA
        if self.game.Player01.movimento in [2,6] and self.game.Player02.movimento in [2,6]:
            self.hx -= 1.5
            eixoX -= 1.5
        # CHAO ESQUERDA
        elif self.game.Player01.movimento in [1,5] and self.game.Player02.movimento in [1,5]:
            self.hx += 1.5
            eixoX += 1.5

        
        # PULO
        if self.game.Player01.pulo > 0 or self.game.Player02.pulo > 0:
            eixoY -= 15

        self.game.Tela.blit(pg.transform.scale(chao, (TELA_LARGURA * 2, 150)), (self.hx, TELA_ALTURA - eixoY))

        if DEBUG:            
            chaotext = f'chão x: {eixoX} y: {eixoY}'
            texto = self.game.fonte.render(chaotext, True, 'Red')                
            self.game.Tela.blit(texto, (5 , TELA_ALTURA_CHAO))

    def modelo(self):        
        dirimage = os.path.join(self.game.Imagens, "modelo.png")
        modelo = pg.image.load(dirimage) 
        modelo = pg.transform.scale(modelo, TELA_RESOLUCAO)     
        modelo = pg.transform.flip(modelo, True, False)
        self.game.Tela.blit(modelo, (0, 0))

    def desenhar(self):
        self.fundo()
        self.chao()        
        # self.modelo()
        