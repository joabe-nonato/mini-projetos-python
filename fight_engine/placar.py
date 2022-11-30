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
        self.cronometro_frame = []
        self.CarregarFrame()
        self.Principal = pg.Rect(0, 10, TELA_LARGURA, 100)
        self.moldura 

    def CarregarFrame(self):
        
        # RECUPERAR TODAS AS IMAGENS
        spritesheet = pg.image.load(os.path.join(self.game.Imagens, self.spritebasico))
        
        for frame in matriz_numero:
            # RECUPERA IMAGEM E ADICIONA NA LISTA
            imagem = spritesheet.subsurface(frame).convert(self.game.superficie)  
            self.cronometro_frame.append(imagem)

        self.moldura = spritesheet.subsurface((17, 82, 11, 11))
        

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
                
        # margem_lateral = 5
        borda_preta = pg.Rect(0,0,400, 40)
        borda_preta.centery = self.Principal.centery
                
        barra_amarela = pg.Rect(0, 0, 400, 34)
        barra_amarela.centery = self.Principal.centery
        
        if esquerda:
            borda_preta.right = (self.Principal.centerx - 55)
            barra_amarela.right = borda_preta.right
            pg.draw.rect(self.game.superficie, AMARELO, barra_amarela) 
        else:    
            borda_preta.left = (self.Principal.centerx + 57)
            barra_amarela.left = borda_preta.left
            pg.draw.rect(self.game.superficie, AMARELO, barra_amarela) 


        pg.draw.rect(self.game.superficie, PRETO, borda_preta, 3)
        
        

        # barra_amarela.left = self.Principal.centerx
        
        

        # branca_largura = (TELA_CENTRO_V - (margem_lateral * 2))        
        
        # x = TELA_CENTRO_V + margem_lateral + 1
        
        # if esquerda:
        #     x = alinhar_centro(branca_largura, TELA_CENTRO_V) 
        
        # 
        # pg.draw.rect(self.game.superficie, BRANCO, bar, 3)

        # pg.draw.rect(self.game.superficie, PRETO, bar) 

        # if esquerda:            
        #     pg.draw.rect(self.game.superficie, AMARELO, (x, bar.y + 3, branca_largura , bar.h - 6))            
        #     pg.draw.rect(self.game.superficie, VERMELHO, (x, bar.y + 3, self.reverter , bar.h - 6)) 
        # else:            
        #     pg.draw.rect(self.game.superficie, AMARELO, (x, bar.y + 3, branca_largura , bar.h - 6)) 
        #     pg.draw.rect(self.game.superficie, VERMELHO, (x, bar.y + 3, saude , bar.h - 6))
        pass
        
    def cronometro(self):
## CRONOMETRO        
        numero_w = 40
        numero_h = 64

        texto_tempo = f'{ int(self.game.Tempo) }'
        # ADICIONAR CASA A ESQUERDA
        if int(self.game.Tempo) < 10:
            texto_tempo = f'0{ int(self.game.Tempo) }'

# BLOCO PRINCIPAL
        dimensao_crono = (numero_w, numero_h)

        sprites = pg.sprite.Group() 
        sprt = pg.sprite.Sprite(sprites)
        sprt.rect = pg.Rect(0, 0, 100, 100)

        sprt.rect.centery = self.Principal.centery
        sprt.rect.centerx = self.Principal.centerx
        sprt.image = self.moldura.convert(self.game.superficie)
        sprt.image = pg.transform.scale(sprt.image, (sprt.rect.w, sprt.rect.h))
        sprites.draw(self.game.superficie)

# # NÚMERO ESQUERDO    
        sprt.rect = pg.Rect(0, 0, numero_w, numero_h)
        sprt.rect.centery = self.Principal.centery
        sprt.rect.right = self.Principal.centerx
        sprt.image = self.cronometro_frame[int(texto_tempo[0])]
        sprt.image = pg.transform.scale(sprt.image, dimensao_crono)
        sprites.draw(self.game.superficie)

        # if DEBUG:
        #     pg.draw.rect(self.game.superficie, AMARELO, sprt.rect,2)

# # NÚMERO DIREITO
        sprt.rect = pg.Rect(0, 0, numero_w, numero_h)
        sprt.rect.centery = self.Principal.centery
        sprt.rect.left = self.Principal.centerx
        sprt.image = self.cronometro_frame[int(texto_tempo[1])]
        sprt.image = pg.transform.scale(sprt.image, dimensao_crono)
        sprites.draw(self.game.superficie)

        # if DEBUG:
        #     pg.draw.rect(self.game.superficie, AMARELO, sprt.rect,2)


    def desenhar(self):
        self.cronometro()
        self.barra_energia(True, self.game.Player01.saude)
        self.barra_energia(False, self.game.Player02.saude)
        
        
        if DEBUG:
            pg.draw.rect(self.game.superficie, AMARELO, self.Principal, 3)
            pg.draw.line(self.game.superficie, AMARELO, (TELA_CENTRO_V, 0), (TELA_CENTRO_V, TELA_ALTURA), 3)
