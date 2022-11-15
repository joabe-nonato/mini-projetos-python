import pygame as pg
from settings import *


def redenderizar(t, cor, objt):
    pg.draw.rect(t, cor, objt, 2)

def criarobjeto(posx, posy, larg, alt, velx = 1, vely = 1):
    return [pg.Rect(posx, posy, larg, alt), [velx, vely]]

def colisalateral(eesquerda, direcao, bloco_esquerda, bloco_direita):
    if eesquerda:
        if (bloco_esquerda.x + bloco_esquerda.w) >= bloco_direita.x:
            return 0
    else:
        if bloco_esquerda.x <= (bloco_direita.x + bloco_direita.w):
            return 0
    
    return direcao

def informacoes(game, cor, msg, left, topo):
    if DEBUG:
        linhas = msg.split(' ')            
        for escrever in linhas:
            texto = game.fonte.render(escrever, True, cor)                        
            game.Tela.blit(texto, (left , topo))
            topo += 17