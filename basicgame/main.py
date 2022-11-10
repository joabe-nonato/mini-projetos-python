import pygame as pg
from  pygame.locals import *
import sys
from settings import *
from map import *
from player import *

# Importar pygame
# Importar locals = Contem constantes e funções 
# Import sys
# Iniciar PyGame

class Game:

    def __init__(self) -> None:
        pg.init()
        self.Tela = pg.display.set_mode(RESOLUCAO)
        self.relogio = pg.time.Clock()
        self.mapa = Mapa(self)
        self.player = Player(self)        
        self.objetos = {}
        
    def eventos(self):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

    def Atualizar(self):   
        self.player.movimento()                    
        pg.display.set_caption(f'Engine Game {self.player.x, self.player.y}')
        self.relogio.tick(FPS)
        # pg.display.update()        
        pg.display.flip()                
                
    def Desenhar(self):
        self.Tela.fill((0,0,0))           
        self.mapa.draw()
        self.player.draw()

    def run(self):
        while True:            
            self.eventos()
            self.Atualizar()
            self.Desenhar()

if __name__ == '__main__':
    game = Game()
    game.run()        