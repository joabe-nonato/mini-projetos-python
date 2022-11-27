import pygame as pg
import os
import sys
from settings import *
from player01 import *
from player02 import *
from stage import *
from placar import *

teclas = [pg.K_p, pg.K_k, pg.K_m, pg.K_l]

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
        
        TELA_RESOLUCAO = self.Tela.get_size()
        self.Topo = 0
        self.Esquerda = 0
        self.superficie = pg.Surface((TELA_RESOLUCAO))                
        self.Palco = pg.Rect(self.Esquerda, self.Topo, self.superficie.get_width(), (self.superficie.get_height() - (self.superficie.get_height() * 0.1)))
        self.chao = self.Palco.bottom

        self.Estagio = Estagio(self)
        self.Placar = Placar(self)

        self.Player01 = Player01(self)
        self.Player02 = Player02(self)
        
        

    def eventos(self):
        
        for evento in pg.event.get():
            if evento.type == pg.KEYDOWN:
                if evento.type == pg.QUIT or evento.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                elif  evento.key in teclas:
                    self.Player01.Golpe(evento.key)
                    self.Player02.Golpe(evento.key)

        self.Player01.eventos()
        self.Player02.eventos()
        

    def atualizar(self):        
        self.Relogio.tick(FPS)
        self.Palco = pg.Rect(self.Esquerda, self.Topo, self.superficie.get_width(), (self.superficie.get_height() - (self.superficie.get_height() * 0.1)))
        self.Tela.blit(self.superficie, [0,0])

        self.Player01.atualizar()
        self.Player02.atualizar()

        self.Placar.atualizar()
        pg.display.flip()
    

    def desenhar(self):
        self.Tela.fill((255,255,255))
        self.superficie.fill(BRANCO)
        if DEBUG:
            pg.draw.rect(self.superficie, PRETO, self.Palco, 1)

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
            