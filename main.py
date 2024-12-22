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

    for i in range(size):
        for j in range(size):
            if mineField.map[j][i].isMine:
                mineField.map[j][i].texture = 11
            elif mineField.map[j][i].texture == 10:
                mineField.map[j][i].texture = 13

def restart(difficulty):
    global sizes
    global size
    global tileSizes
    global tileSize
    global mines
    global width
    global height
    global mineField
    global firstRevealed
    global screen
    global rects
    global textures
    global exploded

    size = sizes[difficulty]
    tileSize = tileSizes[difficulty]

    width = size * tileSize + sizeOffset_x
    height = size * tileSize + sizeOffset_y

    mines = int((size ** 2) / 5) + 1

    firstRevealed = False
    exploded = False

    mineField = map.map(size)
    mineField.placeMines(mines)
    
    for i in range(len(textures)):
        textures[i] = pygame.transform.scale(textures[i],(tileSize,tileSize))

    rects = [[pygame.Rect((i * tileSize + offset_x, j * tileSize + offset_y),(tileSize,tileSize)) for j in range(size)] for i in range(size)]
    
os.system('cls' if os.name == 'nt' else 'clear')

sizes = (8,16,24)
tileSizes = (96,48,32)

size = 5
tileSize = 64

offset_y = 100
offset_x = 0
sizeOffset_y = 100
sizeOffset_x = 0

difficulty = 1
size = sizes[difficulty]
tileSize = tileSizes[difficulty]


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

backgroundColor = pygame.Color(35,173,79)

pygame.init()

pygame.display.set_caption('Pysweeper')

width = size * tileSize + sizeOffset_x
height = size * tileSize + sizeOffset_y

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

mineField = map.map(size)
mineField.placeMines(mines)

rects = [[pygame.Rect((i * tileSize + offset_x, j * tileSize + offset_y),(tileSize,tileSize)) for j in range(size)] for i in range(size)]

pygame.mixer.init()

yay = pygame.mixer.Sound("audio/yay.mp3") # https://pixabay.com/sound-effects/search/yay/
boom = pygame.mixer.Sound("audio/boom.mp3") # https://pixabay.com/sound-effects/search/explosion/

preivousKeyPresses = (False,False,False)
firstRevealed = False
exploded = False

minesLeftFont = pygame.font.Font('freesansbold.ttf', 64)
diffcultyFont = pygame.font.Font('freesansbold.ttf', 16)

button = pygame.image.load("textures/button.png")
button = pygame.transform.scale(button, (96,48))

easyText = diffcultyFont.render("Easy",True,"black")
mediumText = diffcultyFont.render("Medium",True,"black")
hardText = diffcultyFont.render("Hard",True,"black")

easyRect = button.get_rect()
mediumRect = button.get_rect()
hardRect = button.get_rect()
easyTextRect = easyText.get_rect()
mediumTextRect = mediumText.get_rect()
hardTextRect = hardText.get_rect()

easyPos = (70,50)
mediumPos = (176,50)
hardPos = (282,50)

easyRect.center = easyPos
mediumRect.center = mediumPos
hardRect.center = hardPos
easyTextRect.center = easyPos
mediumTextRect.center = mediumPos
hardTextRect.center = hardPos
 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
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
        print("BOOOM\n")
        restart(difficulty)

    mouseKeyPresses = pygame.mouse.get_pressed() # (left, middle, right)
    mousePos = pygame.mouse.get_pos()

    for i in range(size):
        for j in range(size):
            if rects[i][j].collidepoint(mousePos):
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
                                mineField.clear((j,i))
                                break

                    elif mineField.map[j][i].isMine:
                        explode()

                        mineField.map[j][i].texture = 12

                    elif mineField.map[j][i].texture in (9,10):
                        mineField.clear((j,i))
                    else:
                        for k in range(-1,2):
                            for l in range(-1,2):
                                try:
                                    if j + l > -1 and i + k > -1:
                                        if mineField.map[j + l][i + k].isMine:
                                            if not mineField.map[j + l][i + k].isFlagged:
                                                explode()
                                        else:
                                            mineField.clear((j + l, i + k))
                                except: pass

    if mouseKeyPresses[0] and not preivousKeyPresses[0]:
        if easyRect.collidepoint(mousePos):
            difficulty = 0
            restart(difficulty)
        if mediumRect.collidepoint(mousePos):
            difficulty = 1
            restart(difficulty)
        if hardRect.collidepoint(mousePos):
            difficulty = 2
            restart(difficulty)

    preivousKeyPresses = pygame.mouse.get_pressed()

    screen.fill(backgroundColor)

    minesLeft = minesLeftFont.render(str(mineField.minesLeft()),True,"black")
    minesLeftRect = minesLeft.get_rect()
    minesLeftRect.center = (width / 2, 50)

    screen.blit(minesLeft, minesLeftRect)

    screen.blit(button, easyRect)
    screen.blit(easyText, easyTextRect)
    screen.blit(button, mediumRect)
    screen.blit(mediumText, mediumTextRect)
    screen.blit(button, hardRect)
    screen.blit(hardText, hardTextRect)

    for i in range(size):
        for j in range(size):
            screen.blit(textures[mineField.map[i][j].texture],(j * tileSize + offset_x, i * tileSize + offset_y))

    pygame.display.flip()
    clock.tick(60)