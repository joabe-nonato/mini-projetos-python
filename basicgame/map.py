import pygame as pg
from settings import *
from objeto import *

mapeamento = [
    [1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,0,0,2,0,0,0,1],
    [1,0,0,0,0,2,0,1],
    [1,0,0,2,0,0,2,1],
    [1,2,0,0,0,0,0,1],
    [1,0,0,2,0,0,0,1],
    [1,0,2,0,0,2,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1],
]

class Mapa:
    def __init__(self, game) -> None:
        self.game = game
        self.mapeamento = mapeamento
        self.fonte = pg.font.SysFont('arial', 10, False, False)

    def add_obj(self, gm, x, y, value):
        gm.objetos[(x, y)] = value
       
    def draw(self):
        
        for x, row in enumerate(self.mapeamento):
            for y, value in enumerate(row):                

                obj = Objeto()
                obj.largura = BLOCO_LARGURA
                obj.altura = BLOCO_ALTURA
                obj.x = (x * BLOCO_LARGURA)
                obj.y = (y * BLOCO_ALTURA)
                
                if value == 1:       
                    self.add_obj(self.game, obj.x, obj.y, value)                                                                         
                    pg.draw.rect(self.game.Tela, 'white', (obj.x, obj.y, obj.largura, obj.altura), 2)   
                                     
                if value == 2:            
                    self.add_obj(self.game, obj.x, obj.y, value)                                                       
                    pg.draw.rect(self.game.Tela, 'white', (obj.x, obj.y, obj.largura, obj.altura))
                
                if value:       
                    msg = f'x:{obj.x} y:{obj.y}'
                    texto = self.fonte.render(msg, True, 'Red')
                    self.game.Tela.blit(texto, (obj.x + 5, obj.y + 20))
                
                
