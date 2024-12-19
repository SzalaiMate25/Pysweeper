import pygame
import sys
import tile
import map

size = 25
tileSize = 40
mines = int((size ** 2) / 5)

textures = [
    pygame.image.load("textures/cell0.png"),
    pygame.image.load("textures/cell1.png"),
    pygame.image.load("textures/cell2.png"),
    pygame.image.load("textures/cell3.png"),
    pygame.image.load("textures/cell4.png"),
    pygame.image.load("textures/cell5.png"),
    pygame.image.load("textures/cell6.png"),
    pygame.image.load("textures/cell7.png"),
    pygame.image.load("textures/cell8.png"),
    pygame.image.load("textures/cellup.png"),
    pygame.image.load("textures/celldown.png"),
            ]

for i in range(len(textures)):
    textures[i] = pygame.transform.scale(textures[i],(tileSize,tileSize))
    
mineField = map.map(size)
mineField.placeMines(mines)

pygame.init()
screen = pygame.display.set_mode((size * tileSize, size * tileSize))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill("brown")

    for i in range(size):
        for j in range(size):
            screen.blit(textures[mineField.map[i][j].texture],(j * tileSize, i * tileSize))

    mouseKeyPresses = pygame.mouse.get_pressed() # (left, middle, right)

    

    pygame.display.flip()
    clock.tick(60)