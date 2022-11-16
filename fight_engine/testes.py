import pygame
import sys

(width, height) = (800, 600)
pygame.init()
screen = pygame.display.set_mode((width, height))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    


    
    pygame.display.update()

   

        

