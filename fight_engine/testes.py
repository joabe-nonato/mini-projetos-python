import pygame
import sys

(width, height) = (800, 600)
pygame.init()
screen = pygame.display.set_mode((width, height))
image = pygame.image.load("D:\PROJETOS\Python\sfengine\imagens\parede.png").convert_alpha()
masked_result = image.copy()

white_color = (255, 255, 255)
polygon = [(100,100), (700,100), (800,200), (0,200)]

mask_surface = pygame.Surface((width, height))

pygame.draw.polygon(mask_surface, white_color, polygon, 0)

pygame.draw.aalines(mask_surface, white_color, True, polygon)#moderately helps with ugly aliasing

masked_result.blit(mask_surface, (0, 0), None, pygame.BLEND_RGBA_MULT)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(masked_result, (0, 0))
    pygame.draw.polygon(screen, 'Red', [(100,300), (700,300), (800,500), (0,500)], pygame.BLEND_RGBA_MULT)
    pygame.display.update()

   

        

