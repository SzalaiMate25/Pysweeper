import pygame
import sys
import tile
import map
from copy import deepcopy as copy

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
    

pygame.init()
screen = pygame.display.set_mode((size * tileSize, size * tileSize))
clock = pygame.time.Clock()

mineField = map.map(size)
mineField.placeMines(mines)

rects = [[pygame.Rect((i * tileSize, j * tileSize),(tileSize,tileSize)) for j in range(size)] for i in range(size)]

preivousKeyPresses = (False,False,False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill("brown")

    for i in range(size):
        for j in range(size):
            screen.blit(textures[mineField.map[i][j].texture],(j * tileSize, i * tileSize))

    mouseKeyPresses = pygame.mouse.get_pressed() # (left, middle, right)

    for i in range(size):
        for j in range(size):
            if rects[i][j].collidepoint(pygame.mouse.get_pos()):
                if mouseKeyPresses[2] and not preivousKeyPresses[2]:
                    if mineField.map[j][i].isFlagged:
                        mineField.map[j][i].texture = 9
                        mineField.map[j][i].isFlagged = False

                    else:
                        mineField.map[j][i].texture = 10
                        mineField.map[j][i].isFlagged = True

                elif mouseKeyPresses[0] and not preivousKeyPresses[0]:
                    if mineField.map[j][i].isMine:
                        print("BOOOM")
                        sys.exit()

                    else:
                        mineField.clear((j,i))

    preivousKeyPresses = pygame.mouse.get_pressed()

    finished = True

    for row in mineField.map:
        for cell in row:
            if cell.texture == 9 or cell.isMine != cell.isFlagged:
                finished = False
    if finished:
        print("You win!")
        sys.exit()
        

    pygame.display.flip()
    clock.tick(60)