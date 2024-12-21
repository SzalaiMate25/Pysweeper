import pygame
import sys
import tile
import map
import time
from copy import deepcopy as copy

size = 5
tileSize = 64
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
    pygame.image.load("textures/cellmine.png"),
    pygame.image.load("textures/exploded.png"),
            ]

for i in range(len(textures)):
    textures[i] = pygame.transform.scale(textures[i],(tileSize,tileSize))
    

pygame.init()
screen = pygame.display.set_mode((size * tileSize, size * tileSize))
clock = pygame.time.Clock()

mineField = map.map(size)
mineField.placeMines(mines)

rects = [[pygame.Rect((i * tileSize, j * tileSize),(tileSize,tileSize)) for j in range(size)] for i in range(size)]

pygame.mixer.init()

yay = pygame.mixer.Sound("audio/yay.mp3") # https://pixabay.com/sound-effects/search/yay/
boom = pygame.mixer.Sound("audio/boom.mp3") # https://pixabay.com/sound-effects/search/explosion/

preivousKeyPresses = (False,False,False)
firstRevealed = False
exploded = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
        finished = True

    for row in mineField.map:
        for cell in row:
            if cell.texture == 9 or cell.isMine != cell.isFlagged:
                finished = False
                
    if finished:
        pygame.mixer.Sound.play(yay)
        time.sleep(3)
        print("You win!")
        sys.exit()

    if exploded:
        pygame.mixer.Sound.play(boom)
        time.sleep(3)
        print("BOOOM")
        sys.exit()

    mouseKeyPresses = pygame.mouse.get_pressed() # (left, middle, right)

    for i in range(size):
        for j in range(size):
            if rects[i][j].collidepoint(pygame.mouse.get_pos()):
                if mouseKeyPresses[2] and not preivousKeyPresses[2] and mineField.map[j][i].texture in (9,10):
                    if mineField.map[j][i].isFlagged:
                        mineField.map[j][i].texture = 9
                        mineField.map[j][i].isFlagged = False

                    else:
                        mineField.map[j][i].texture = 10
                        mineField.map[j][i].isFlagged = True

                elif mouseKeyPresses[0] and not preivousKeyPresses[0]:
                    if not firstRevealed:
                        while True:
                            if mineField.getAdjacent((j,i)) != 0:
                                mineField = map.map(size)
                                mineField.placeMines(mines)

                            else:
                                firstRevealed = True
                                break

                    if mineField.map[j][i].isMine:
                        exploded = True

                        for k in range(size):
                            for l in range(size):
                                if mineField.map[k][l].isMine:
                                    mineField.map[k][l].texture = 11

                        mineField.map[j][i].texture = 12

                    else:
                        mineField.clear((j,i))

    preivousKeyPresses = pygame.mouse.get_pressed()

    screen.fill("green")

    for i in range(size):
        for j in range(size):
            screen.blit(textures[mineField.map[i][j].texture],(j * tileSize, i * tileSize))

    pygame.display.flip()
    clock.tick(60)