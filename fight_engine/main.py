import pygame as pg
import os
import sys
from settings import *
from player01 import *
from player02 import *
from stage import *
from placar import *


class Game:
    def __init__(self) -> None:
        pg.init()
        self.continuar = True
        self.Tela = pg.display.set_mode(TELA_RESOLUCAO)
        # self.Tela = pg.display.set_mode()
        self.fonte = pg.font.SysFont('arial', 19, True, False)
        self.Relogio = pg.time.Clock()
        self.Tempo = TEMPO_LUTA
        self.luta_encerrada = False
        self.Diretorio = os.path.dirname(__file__)
        self.Imagens = os.path.join(self.Diretorio, 'imagens')
        
        # TELA_RESOLUCAO = self.Tela.get_size()
        self.Topo = 0
        self.Esquerda = 0
        self.superficie = pg.Surface(TELA_RESOLUCAO)
        self.Palco = pg.Rect(self.Esquerda, self.Topo, self.superficie.get_width(), (self.superficie.get_height() - (self.superficie.get_height() * 0.1)))
        self.chao = self.Palco.bottom

        self.Estagio = Estagio(self)
        self.Placar = Placar(self)
        self.Player01 = Player01(self)
        self.Player02 = Player02(self)
        

    def eventos(self):
        
        # pressionado = pg.key.get_pressed()

        for evg in pg.event.get():
            if evg.type == pg.QUIT:
                self.continuar = False
            elif (evg.type == pg.KEYDOWN or evg.type == pg.KEYUP) and evg.key == pg.K_ESCAPE:
                    self.continuar = False
            elif (evg.type == pg.KEYDOWN or evg.type == pg.KEYUP) or True in pg.key.get_pressed():
                self.Player01.eventos(evg)
                self.Player02.eventos(evg)
        
        if self.continuar == False:
            pg.quit()
            sys.exit()

    def atualizar(self):        
        self.Relogio.tick(FPS)
        self.Palco = pg.Rect(self.Esquerda, self.Topo, self.superficie.get_width(), (self.superficie.get_height() - (self.superficie.get_height() * 0.1)))
        self.Tela.blit(self.superficie, [0,0])

        self.Player01.atualizar()
        self.Player02.atualizar()

        self.Placar.atualizar()
        pg.display.flip()
    

    def desenhar(self):
        self.Tela.fill(ROSA)
        self.superficie.fill(ROSA)
        if DEBUG:
            pg.draw.rect(self.superficie, PRETO, self.Palco, 1)

        self.Estagio.desenhar() 
        self.Placar.desenhar()       
        self.Player01.desenhar() 
        self.Player02.desenhar()     

    def executar(self):    
        while self.continuar:
            self.eventos()
            self.atualizar()
            self.desenhar()

if __name__ == '__main__':
    game = Game()
    game.executar()
            