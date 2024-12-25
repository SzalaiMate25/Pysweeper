import pygame
import sys
import map
import time
from copy import deepcopy as copy
import os
import highscoreManager
import timer
import pyAssets

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
    global exploded
    global timerText

    size = sizes[difficulty]
    tileSize = tileSizes[difficulty]

    width = size * tileSize + sizeOffset_x
    height = size * tileSize + sizeOffset_y

    mines = int((size ** 2) / 5) + 1

    firstRevealed = False
    exploded = False

    mineField = map.map(size)
    mineField.placeMines(mines)

    pyAssets.loadTextures(tileSize, offset_x, offset_y, size)

    timerText = ""
    
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

width = size * tileSize + sizeOffset_x
height = size * tileSize + sizeOffset_y

pyAssets.loadTextures(tileSize, offset_x, offset_y, size)
pyAssets.init(width, height)

mineField = map.map(size)
mineField.placeMines(mines)

preivousKeyPresses = (False,False,False)
firstRevealed = False
exploded = False

run = False

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
        pyAssets.playSound("yay")
        highscoreManager.addHighscore(difficulty, round(timer.getTimer(), 2))
        timer.stop()
        time.sleep(3)
        run = False
        print("You win!")
        sys.exit()

    if exploded:
        pyAssets.playSound("boom")
        time.sleep(3)
        run = False
        print("BOOOM\n")
        restart(difficulty)

    mouseKeyPresses = pygame.mouse.get_pressed() # (left, middle, right)
    mousePos = pygame.mouse.get_pos()

    for i in range(size):
        for j in range(size):
            if pyAssets.rects[i][j].collidepoint(mousePos):
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
                                timer.startTimer()
                                run = True
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
        if pyAssets.easyRect.collidepoint(mousePos):
            difficulty = 0
            restart(difficulty)
        if pyAssets.mediumRect.collidepoint(mousePos):
            difficulty = 1
            restart(difficulty)
        if pyAssets.hardRect.collidepoint(mousePos):
            difficulty = 2
            restart(difficulty)

    preivousKeyPresses = pygame.mouse.get_pressed()

    pyAssets.drawGUI(mineField.minesLeft(), 
                     run, timer.convertTime(timer.getTimer(), 1), 
                     highscoreManager.getHighscores()[difficulty],)
    pyAssets.drawMinefield(mineField, size, tileSize, offset_x, offset_y)
    

    pygame.display.flip()
    pyAssets.clock.tick(60)