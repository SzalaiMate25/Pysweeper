import pygame
import timer
import sys

def loadTextures(tileSize, offset_x, offset_y, size):
    global textures, rects, backgroundColor, button, timerBackground, finishWindow, closeButton, largeButton

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

    rects = [[pygame.Rect((i * tileSize + offset_x, j * tileSize + offset_y),(tileSize,tileSize)) for j in range(size)] for i in range(size)]

    button = pygame.transform.scale(pygame.image.load("textures/button.png"), (96,48))
    timerBackground = pygame.transform.scale(pygame.image.load("textures/timer.png"), (96,48))

    finishWindow = pygame.image.load("textures/finishwindow.png")
    closeButton = pygame.image.load("textures/closebutton.png")
    largeButton = pygame.image.load("textures/largebutton.png")

# Misc
def loadMisc():
    global backgroundColor

    backgroundColor = pygame.Color(35,173,79)

# Fonts
def loadFonts():
    global minesLeftFont, GUIfont, titleFont, smallTitleFont, largeTitleFont, difficultyFont

    minesLeftFont = pygame.font.Font('freesansbold.ttf', 64)
    GUIfont = pygame.font.Font('freesansbold.ttf', 22)
    titleFont = pygame.font.Font('freesansbold.ttf', 42)
    smallTitleFont = pygame.font.Font('freesansbold.ttf', 32)
    largeTitleFont = pygame.font.Font('freesansbold.ttf', 72)
    difficultyFont = pygame.font.Font('freesansbold.ttf', 52)

# Texts
def loadTexts():
    global easyText, mediumText, hardText, bestTimeTitle, congratulationsText, youWinText, difficultyTitleText, difficultyTexts, yourTimeTitle, windowBestTimeTitle
    global playAgainText, quitText, resetText, highscoreText

    easyText = GUIfont.render("Easy",True,"black")
    mediumText = GUIfont.render("Medium",True,"black")
    hardText = GUIfont.render("Hard",True,"black")
    bestTimeTitle = GUIfont.render("Best Time:",True,"black")

    # Finish window

    congratulationsText = titleFont.render("CONGRATULATIONS!",True,"black")
    youWinText = smallTitleFont.render("You Win!",True,"black")

    difficultyTitleText = titleFont.render("Difficulty:",True,"black")
    difficultyTexts = [
        difficultyFont.render("Easy",True,"black"),
        difficultyFont.render("Medium",True,"black"),
        difficultyFont.render("Hard",True,"black")
    ]

    yourTimeTitle = titleFont.render("Your Time:",True,"black")
    windowBestTimeTitle = smallTitleFont.render("Best Time:",True,"black")

    playAgainText = GUIfont.render("Play Again",True,"black")
    quitText = GUIfont.render("Quit",True,"black")
    resetText = GUIfont.render("Reset",True,"black")
    highscoreText = GUIfont.render("Highscores",True,"black")

# GUI rects

# Positions

def loadPos(width):
    global easyPos, mediumPos, hardPos, timerPos
    global bestTimeTitlePos, bestTimePos, congratulationsPos, youWinPos, difficultyTitlePos, difficultyPos, yourTimeTitlePos, yourTimePos, windowBestTimeTitlePos, windowBestTimePos
    global closeButtonPos, playAgainPos, quitPos, resetPos, highscorePos, resetMiddlePos

    easyPos = (70,50)
    mediumPos = (176,50)
    hardPos = (282,50)

    timerPos = (width - 70,50)

    bestTimeTitlePos = (width - 235,40)
    bestTimePos = (width - 235,70)

    congratulationsPos = (width / 2, 150)
    youWinPos = (width / 2, 200)

    difficultyTitlePos = (width / 2, 275)
    difficultyPos = (width / 2, 325)

    yourTimeTitlePos = (width / 2, 390)
    yourTimePos = (width / 2, 440)

    windowBestTimeTitlePos = (width / 2, 505)
    windowBestTimePos = (width / 2, 555)

    closeButtonPos = (668,100)

    playAgainPos = (width / 2, 700)
    quitPos = (width / 2 - 178, 700)
    resetPos = (width / 2 + 178, 685)
    resetMiddlePos = (width / 2 + 178, 700)
    highscorePos =  (width / 2 + 178, 715)

def loadButtonRects():
    global easyRect, mediumRect, hardRect, easyTextRect, mediumTextRect, hardTextRect
    global closeButtonRect, playAgainButtonRect, quitButtonRect, resetButtonRect, playAgainTextRect, quitTextRect, resetTextRect, highscoreTextRect

    easyRect = button.get_rect()
    mediumRect = button.get_rect()
    hardRect = button.get_rect()

    easyRect.center = easyPos
    mediumRect.center = mediumPos
    hardRect.center = hardPos

    easyTextRect = easyText.get_rect()
    mediumTextRect = mediumText.get_rect()
    hardTextRect = hardText.get_rect()

    easyTextRect.center = easyPos
    mediumTextRect.center = mediumPos
    hardTextRect.center = hardPos

    closeButtonRect = closeButton.get_rect()

    playAgainButtonRect = largeButton.get_rect()
    quitButtonRect = largeButton.get_rect()
    resetButtonRect = largeButton.get_rect()

    closeButtonRect.center = closeButtonPos

    playAgainButtonRect.center = playAgainPos
    quitButtonRect.center = quitPos
    resetButtonRect.center = resetMiddlePos

    playAgainTextRect = playAgainText.get_rect()
    quitTextRect = quitText.get_rect()
    resetTextRect = resetText.get_rect()
    highscoreTextRect = highscoreText.get_rect()

    playAgainTextRect.center = playAgainPos
    quitTextRect.center = quitPos
    resetTextRect.center = resetPos
    highscoreTextRect.center = highscorePos

def loadRects():
    global timerBackRect, bestTimeTitleRect, congratulationsRect, youWinRect, difficultyTitleRect, yourTimeTitleRect, difficultyRects, windowBestTimeTitleRect

    # Timer

    timerBackRect = timerBackground.get_rect()
    timerBackRect.center = timerPos

    # Best Time

    bestTimeTitleRect = bestTimeTitle.get_rect()
    bestTimeTitleRect.center = bestTimeTitlePos

    # Finish window

    congratulationsRect = congratulationsText.get_rect()
    youWinRect = youWinText.get_rect()
    difficultyTitleRect = difficultyTitleText.get_rect()
    yourTimeTitleRect = yourTimeTitle.get_rect()

    difficultyRects = [text.get_rect() for text in difficultyTexts]

    windowBestTimeTitleRect = windowBestTimeTitle.get_rect()

    congratulationsRect.center = congratulationsPos
    youWinRect.center = youWinPos
    difficultyTitleRect.center = difficultyTitlePos
    yourTimeTitleRect.center = yourTimeTitlePos

    for i in range(3):
        difficultyRects[i].center = difficultyPos

    windowBestTimeTitleRect.center = windowBestTimeTitlePos

def loadSounds():
    global soundNames, sounds

    # Source: https://pixabay.com/sound-effects

    soundNames = ["yay","boom"]
    sounds = [pygame.mixer.Sound("audio/yay.mp3"), pygame.mixer.Sound("audio/boom.mp3")]

# Functions

def init(setWidth, setHeight):
    global screen, clock, width, height

    width = setWidth
    height = setHeight

    pygame.init()
    pygame.mixer.init()

    pygame.display.set_caption('Pysweeper')
    pygame.display.set_icon(pygame.image.load("textures/icon.png"))

    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    loadMisc()
    loadFonts()
    loadTexts()
    loadPos(width)
    loadButtonRects()
    loadRects()
    loadSounds()

def playSound(sound):
    pygame.mixer.Sound.play(sounds[soundNames.index(sound)])

# Draw functions

def drawMinesLeft(minesLeft):
    minesLeftText = minesLeftFont.render(str(minesLeft),True,"black")
    minesLeftRect = minesLeftText.get_rect()
    minesLeftRect.center = (width / 2, 50)

    screen.blit(minesLeftText, minesLeftRect)

def drawButtons():
    # Buttons
    screen.blit(button, easyRect)
    screen.blit(button, mediumRect)
    screen.blit(button, hardRect)

    # Text
    screen.blit(easyText, easyTextRect)
    screen.blit(mediumText, mediumTextRect)
    screen.blit(hardText, hardTextRect)

def drawTimer(run, timer):

    if run:
        timerText = GUIfont.render(timer,True,"green")
    else:
        timerText = GUIfont.render("00:00",True,"green")

    timerTextRect = timerText.get_rect()
    timerTextRect.center = timerPos

    screen.blit(timerBackground, timerBackRect)
    screen.blit(timerText, timerTextRect)

def drawBestTime(bestTime):
    if bestTime == "-":
        bestTimeText = GUIfont.render("-",True,"black")
    else:
        bestTimeText = GUIfont.render(timer.convertTime(float(bestTime),1),True,"black")

    bestTimeRect = bestTimeText.get_rect()
    bestTimeRect.center = bestTimePos

    screen.blit(bestTimeTitle, bestTimeTitleRect)
    screen.blit(bestTimeText, bestTimeRect)

def drawMinefield(mineField, size, tileSize, offset_x, offset_y):
    for i in range(size):
        for j in range(size):
            screen.blit(textures[mineField.map[i][j].texture],(j * tileSize + offset_x, i * tileSize + offset_y))

def drawGUI(minesLeft, run, timer, bestTime):
    screen.fill(backgroundColor)

    drawMinesLeft(minesLeft)
    drawButtons()
    drawTimer(run, timer)
    drawBestTime(bestTime)

def drawFinishWindow(difficulty, currentTime, bestTime):

    currentTimeText = largeTitleFont.render(timer.convertTime(currentTime, 1),True,"black")

    currentTimeRect = currentTimeText.get_rect()
    currentTimeRect.center = yourTimePos

    if bestTime == "-":
        bestTimeText = titleFont.render("-",True,"black")
    else:
        bestTimeText = titleFont.render(timer.convertTime(float(bestTime), 1),True,"black")

    bestTimeRect = bestTimeText.get_rect()
    bestTimeRect.center = windowBestTimePos


    screen.blit(finishWindow, (100, 100))

    screen.blit(congratulationsText, congratulationsRect)
    screen.blit(youWinText, youWinRect)

    screen.blit(difficultyTitleText, difficultyTitleRect)
    screen.blit(difficultyTexts[difficulty], difficultyRects[difficulty])

    screen.blit(yourTimeTitle, yourTimeTitleRect)
    screen.blit(currentTimeText, currentTimeRect)

    screen.blit(windowBestTimeTitle, windowBestTimeTitleRect)
    screen.blit(bestTimeText, bestTimeRect)

    screen.blit(closeButton, closeButtonRect)

    screen.blit(largeButton, playAgainButtonRect)
    screen.blit(largeButton, quitButtonRect)
    screen.blit(largeButton, resetButtonRect)

    screen.blit(playAgainText, playAgainTextRect)
    screen.blit(quitText, quitTextRect)
    screen.blit(resetText, resetTextRect)
    screen.blit(highscoreText, highscoreTextRect)

    mouseKeyPresses = pygame.mouse.get_pressed() # (left, middle, right)
    mousePos = pygame.mouse.get_pos()

    if mouseKeyPresses[0]:
        if closeButtonRect.collidepoint(mousePos):
            return 1
        elif playAgainButtonRect.collidepoint(mousePos):
            return 2
        elif quitButtonRect.collidepoint(mousePos):
            return 3
        elif resetButtonRect.collidepoint(mousePos):
            return 4
    return 0