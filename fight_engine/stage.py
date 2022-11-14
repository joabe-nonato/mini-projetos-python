import pygame as pg
import os
from settings import *

class Estagio:

    def __init__(self, game) -> None:
        self.game = game
        self.hx = ((TELA_LARGURA // 2) * -1)
        
    def fundo(self):
        bckgrd = pg.image.load(os.path.join("D:\PROJETOS\Python\sfengine\imagens", "fundo.png"))
        eixoX = (-400 - (self.game.Player01.P1.x * (0.2)))        

        eixoY = 10

        # if self.game.Player01.pulo == 1:
        #     eixoY += 10
        # elif self.game.Player01.pulo == 0:
        #     eixoY = 10

        self.game.Tela.blit(pg.transform.scale(bckgrd, (TELA_LARGURA * 2, TELA_ALTURA - 90)), (eixoX, eixoY))

    def chao(self):
        chao = pg.image.load("D:\PROJETOS\Python\sfengine\imagens\chao.png")
        chaox = (((TELA_LARGURA // 2) * -1) - (self.game.Player01.P1.x -0.5))
        eixoY = 100

        if self.game.Player01.direcao == 1 and self.hx > 0:
            self.hx += 1
        elif self.game.Player01.direcao == 2 and self.hx < (TELA_LARGURA):
            self.hx -= 1

        if self.game.Player01.pulo == 1:
            eixoY -= 10
        elif self.game.Player01.pulo == 0:
            eixoY = 100

        self.game.Tela.blit(pg.transform.scale(chao, (TELA_LARGURA * 2, 100)), (self.hx, TELA_ALTURA - eixoY))

    def desenhar(self):
        self.fundo()
        self.chao()        
        