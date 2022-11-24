import pygame as pg
import os
from settings import *



class Estagio:

    def __init__(self, game) -> None:
        self.game = game
        self.top = 0
        self.hx = ((TELA_LARGURA // 2) * -1)
        self.dirimage = os.path.join(self.game.Imagens, "tatame.png")
        self.bckgrd = pg.image.load(self.dirimage)
        self.chaoImg = pg.image.load(os.path.join(self.game.Imagens, "chao.png"))
        
    def fundo(self):        
        # dirimage = os.path.join(self.game.Imagens, "fundo.png")
        eixoX = (-400 - (self.game.Player01.BlocoMov.x * (0.2)))       

        eixoY = self.game.Palco.top

        self.game.superficie.blit(pg.transform.scale(self.bckgrd, (TELA_LARGURA * 2, self.game.Palco.h)), (eixoX, eixoY))


    def chao(self):                
        eixoY = self.game.Palco.bottom
        eixoX = self.game.Palco.centerx

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
            eixoY += 15
            self.game.Palco.top -+ 15
        
        bloco = pg.Rect(0, 0, TELA_LARGURA + (TELA_LARGURA // 2), 150)
        bloco.centerx = eixoX
        bloco.centery = eixoY

        self.game.superficie.blit(pg.transform.scale(self.chaoImg, (bloco.w, bloco.h)), (bloco.x, bloco.y))

        if DEBUG:            
            chaotext = f'chão x: {eixoX} y: {eixoY}'
            texto = self.game.fonte.render(chaotext, True, 'Red')                
            self.game.superficie.blit(texto, (5 , self.game.Palco.bottom))

    def modelo(self):        
        dirimage = os.path.join(self.game.Imagens, "modelo.png")
        modelo = pg.image.load(dirimage) 
        # modelo = pg.transform.scale(modelo, TELA_RESOLUCAO)     
        # modelo = pg.transform.flip(modelo, True, False)
        self.game.superficie.blit(modelo, (0, 0))

    def desenhar(self):
        self.fundo()
        self.chao()        
        # self.modelo()
        