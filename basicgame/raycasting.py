# import pygame as pg
# import sys

# LARGURA = 500
# ALTURA = 400

# pg.init()
# relogio = pg.time.Clock()
# continuar = True

# Tela = pg.display.set_mode((LARGURA, ALTURA))

# o1 = [pg.Rect(100,100,50,50),'Red', [-2,3]]
# o2 = [pg.Rect(200,200,50,60),'Blue', [3,-2]]
# o3 = [pg.Rect(300,300,60,50),'Green', [2,-3]]

# p1 = [pg.Rect(400,250,50,50),'Yellow', [-3,3]]

# objetos = [o1, o2, o3, p1]

# def mover(figura):
#     borda_esquerda = 0
#     borda_superior = 0
#     borda_direita = LARGURA
#     borda_inferior = ALTURA
    
#     # colide = False
#     # for o in objetos:        
#     #     colide = pg.Rect.colliderect(figura[0], o[0])

#     if figura[0].top < borda_superior or figura[0].bottom > borda_inferior:
#         figura[2][1] = -figura[2][1]

#     if figura[0].left < borda_esquerda or figura[0].right > borda_direita:
#         figura[2][0] = -figura[2][0]
    
#     figura[0].x += figura[2][0]
#     figura[0].y += figura[2][1]

# def eventos():
#     global continuar
#     for evento in pg.event.get():
#         if evento.type == pg.QUIT:
#             continuar = False
#             pg.quit()
#             sys.exit()

# def atualizar():
#     Tela.fill('Black')
#     for obj in objetos:
#         mover(obj)
#         pg.draw.rect(Tela, obj[1], obj[0])        
            
#     pg.display.flip()
#     relogio.tick(90)

# while continuar:
#     eventos()
#     atualizar()
    

