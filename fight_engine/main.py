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
        # self.Tela = pg.display.set_mode(TELA_RESOLUCAO)
        self.Tela = pg.display.set_mode()
        self.fonte = pg.font.SysFont('arial', 19, True, False)
        self.Relogio = pg.time.Clock()
        self.Tempo = TEMPO_LUTA
        self.luta_encerrada = False
        self.Diretorio = os.path.dirname(__file__)
        self.Imagens = os.path.join(self.Diretorio, 'imagens')
        self.Objetos = []
        self.Player01 = Player01(self)
        self.Player02 = Player02(self)
        self.Estagio = Estagio(self)
        self.Placar = Placar(self)

        TELA_RESOLUCAO = self.Tela.get_size()
        # print(TELA_RESOLUCAO, 'resolução')

    def eventos(self):
        global ev
        tcl = pg.key.get_pressed()

        for evento in pg.event.get():
            if evento.type == pg.QUIT or tcl[pg.K_ESCAPE] :
                pg.quit()
                sys.exit()
            
            elif evento.type == pg.KEYUP:
                self.Player01.Golpe(tcl)
                self.Player02.Golpe(tcl)

        self.Player01.eventos()
        self.Player02.eventos()
        
    def atualizar(self):        
        self.Relogio.tick(FPS)

        self.Player01.atualizar()
        self.Player02.atualizar()
        
        self.Placar.atualizar()
        pg.display.flip()
    

    def desenhar(self):
        self.Tela.fill((255,255,255))

        self.Estagio.desenhar() 
        self.Placar.desenhar()       
        self.Player01.desenhar() 
        self.Player02.desenhar()     
        
        
    def executar(self):    
        while True:
            self.eventos()
            self.atualizar()
            self.desenhar()

if __name__ == '__main__':
    game = Game()
    game.executar()
            