import pygame
import timer

def loadTextures(tileSize, offset_x, offset_y, size):
    global textures, rects, backgroundColor, button, timerBackground

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

# Misc
def loadMisc():
    global backgroundColor

    backgroundColor = pygame.Color(35,173,79)

# Fonts
def loadFonts():
    global minesLeftFont, GUIfont

    minesLeftFont = pygame.font.Font('freesansbold.ttf', 64)
    GUIfont = pygame.font.Font('freesansbold.ttf', 22)

# Texts
def loadTexts():
    global easyText, mediumText, hardText, bestTimeTitle

    easyText = GUIfont.render("Easy",True,"black")
    mediumText = GUIfont.render("Medium",True,"black")
    hardText = GUIfont.render("Hard",True,"black")
    bestTimeTitle = GUIfont.render("Best Time:",True,"black")

# GUI rects

# Positions

def loadPos(width):
    global easyPos, mediumPos, hardPos, timerPos, bestTimeTitlePos, bestTimePos

    easyPos = (70,50)
    mediumPos = (176,50)
    hardPos = (282,50)

    timerPos = (width - 70,50)

    bestTimeTitlePos = (width - 235,40)
    bestTimePos = (width - 235,70)

def loadButtonRects():
    global easyRect, mediumRect, hardRect, easyTextRect, mediumTextRect, hardTextRect

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

def loadRects():
    global timerBackRect, bestTimeTitleRect

    # Timer
    timerBackRect = timerBackground.get_rect()
    timerBackRect.center = timerPos

    # Best Time
    bestTimeTitleRect = bestTimeTitle.get_rect()
    bestTimeTitleRect.center = bestTimeTitlePos


def loadSounds():
    global soundNames, sounds

    # Source: https://pixabay.com/sound-effects

    soundNames = ["yay","boom"]
    sounds = [pygame.mixer.Sound("audio/yay.mp3"), pygame.mixer.Sound("audio/boom.mp3")]

# Functions

def init(setWidth, setHeight):
    global screen, clock, width, Height

    width = setWidth
    height = setHeight
    print(width, height)

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

def drawFinishWindow():
    pass 