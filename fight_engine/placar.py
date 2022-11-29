import pygame as pg
from essencial import *
from data import *

class Placar:
    def __init__(self, game):
        self.game = game
        self.reverter = 0
        self.velocidade = 1
        self.barra_largura_padrao = BARRA_ENERGIA
        self.barra_altura = 40        
        self.barra_y = 40
        self.spritebasico = spritebasico
        self.cronometo_frame = []
        self.CarregarFrame()

    def CarregarFrame(self):
        
        # RECUPERAR TODAS AS IMAGENS
        spritesheet = pg.image.load(os.path.join(self.game.Imagens, self.spritebasico))
        
        for frame in matriz_numero:
            # RECUPERA IMAGEM E ADICIONA NA LISTA
            imagem = spritesheet.subsurface(frame)  
            self.cronometo_frame.append(imagem)
        

    def atualizar(self):       
    #    CRONOMETRO
        if self.game.Tempo == -99:
            self.game.Tempo = 0
        elif self.game.Tempo > 0 and self.game.Player01.saude > 0 and self.game.Player02.saude > 0:
            self.game.Tempo -= 0.035
        elif self.game.Tempo > 0 and (self.game.Player01.saude <= 0 or self.game.Player02.saude <= 0):
            self.game.luta_encerrada = True
        else:
            self.game.luta_encerrada = True

        # # TESTE TESTE TESTE        
        # if self.game.Tempo > 0 and self.game.Player01.saude > 0 and self.game.Player02.saude > 0:
        #     self.reverter += int(self.velocidade)
        #     self.game.Player01.saude -= int(self.velocidade)
        #     self.game.Player02.saude -= int(self.velocidade)

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
        
    def cronometro(self):
## CRONOMETRO        
        numero_w = 45
        numero_h = 78
        texto_tempo = f'{ int(self.game.Tempo) }'

        # ADICIONAR CASA A ESQUERDA
        if int(self.game.Tempo) < 10:
            texto_tempo = f'0{ int(self.game.Tempo) }'

        crono_rect = pg.Rect(0, 0 , (numero_w + 55), (numero_h + 10))
        crono_rect.centerx = self.game.Palco.centerx
        crono_rect.top = self.barra_y
        pg.draw.rect(self.game.superficie, PRETO, crono_rect)

        dimensao_crono = (numero_w, numero_h)
        sprites = pg.sprite.Group() 
        sprt = pg.sprite.Sprite(sprites)
        sprt.rect = pg.Rect(0, 0, numero_w, numero_h)

# NÚMERO ESQUERDO        
        sprt.rect.centery = crono_rect.centery
        sprt.rect.right = crono_rect.centerx
        sprt.image = self.cronometo_frame[int(texto_tempo[0])]
        sprt.image = pg.transform.scale(sprt.image, dimensao_crono)
        sprites.draw(self.game.superficie)
        # pg.draw.rect(self.game.superficie, AMARELO, sprt.rect,2)

# NÚMERO DIREITO
        sprt.rect.centery = crono_rect.centery
        sprt.rect.left = crono_rect.centerx
        sprt.image = self.cronometo_frame[int(texto_tempo[1])]
        sprt.image = pg.transform.scale(sprt.image, dimensao_crono)
        sprites.draw(self.game.superficie)
        # pg.draw.rect(self.game.superficie, AMARELO, sprt.rect,2)


    def desenhar(self):

        self.barra_energia(True, self.game.Player01.saude)
        self.barra_energia(False, self.game.Player02.saude)
        self.cronometro()
        

        if DEBUG:
            pg.draw.line(self.game.superficie, 'White', (TELA_CENTRO_V, 0), (TELA_CENTRO_V, TELA_ALTURA), 3)
