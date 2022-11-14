import pygame as pg
import os
import sys
from settings import *
from player01 import *
from stage import *

class Game:
    def __init__(self) -> None:
        pg.init()
        self.Tela = pg.display.set_mode(TELA_RESOLUCAO)
        self.fonte = pg.font.SysFont('arial', 12, True, False)
        self.Relogio = pg.time.Clock()
        self.Diretorio = os.path.basename(__file__)
        self.Imagens = os.path.join(self.Diretorio, 'imagens')
        self.Objetos = []
        self.Player01 = Player01(self)
        self.Estagio = Estagio(self)

    def eventos(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                sys.exit()

        self.Player01.eventos()

    def atualizar(self):        
        self.Player01.atualizar()
        self.Relogio.tick(FPS)
        pg.display.flip()

    def desenhar(self):
        self.Tela.fill((255,255,255))
        self.Estagio.desenhar() 
        self.Player01.desenhar()       
        

    def executar(self):    
        while True:
            self.eventos()
            self.atualizar()
            self.desenhar()

if __name__ == '__main__':
    game = Game()
    game.executar()
            