import pygame as pg


def redenderizar(t, cor, objt):
    pg.draw.rect(t, cor, objt, 2)

def criarobjeto(posx, posy, larg, alt, velx = 1, vely = 1):
    return [pg.Rect(posx, posy, larg, alt), [velx, vely]]