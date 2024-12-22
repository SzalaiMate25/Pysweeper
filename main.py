import pygame
import sys
import tile
import map
import time
from copy import deepcopy as copy
import os

def explode():
    global exploded
    global mineField
    global size

    exploded = True

    for k in range(size):
        for l in range(size):
            if mineField.map[k][l].isMine:
                mineField.map[k][l].texture = 11
            elif mineField.map[k][l].texture == 10:
                mineField.map[k][l].texture = 13

os.system('cls' if os.name == 'nt' else 'clear')

sizes = (8,16,25)
tileSizes = (96,48,32)

size = 5
tileSize = 64

while True:
    try:
        difficulty = int(input("Enter difficulty (1-3): "))
        if difficulty == -1:
            break
        if difficulty == 0:
            try:
                size = int(input("Enter custom size: "))
                if size < 1:
                    print("Size cannot be less than 1")
                else:
                    if size < 10:
                        tileSize = 96
                    elif size < 20:
                        tileSize = 48
                    elif size < 32:
                        tileSize = 32
                    else:
                        tileSize = 24
                    break
            except:
                print("Invalid input")
        if difficulty in (1,2,3):
            size = sizes[difficulty - 1]
            tileSize = tileSizes[difficulty - 1]
            break
        else: 
            print("Difficulty not in range")
    except:
        print("Invalid input")

if difficulty == -1:
    sys.exit()

mines = int((size ** 2) / 5) + 1

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
    pygame.image.load("textures/falseflagged.png"),
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
                        explode()

                        mineField.map[j][i].texture = 12

                    elif mineField.map[j][i].texture in (9,10):
                        mineField.clear((j,i))
                    else:
                        for k in range(-1,2):
                            for l in range(-1,2):
                                if mineField.map[j + l][i + k].isMine:
                                    if not mineField.map[j + l][i + k].isFlagged:
                                        explode()
                                else:
                                    mineField.clear((j + l, i + k))

    preivousKeyPresses = pygame.mouse.get_pressed()

    screen.fill("green")

    for i in range(size):
        for j in range(size):
            screen.blit(textures[mineField.map[i][j].texture],(j * tileSize, i * tileSize))

    pygame.display.flip()
    clock.tick(60)