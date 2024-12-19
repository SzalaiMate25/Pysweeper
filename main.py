import pygame
import sys
import tile
import map

pygame.init()
screen = pygame.display.set_mode((800,800)) # one cell is 32x32, the entire thing is 25*25 for now
clock = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill("brown")



    pygame.display.flip()
    clock.tick(60)