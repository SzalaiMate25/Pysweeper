def resetHighscores():
    highscoreFile = open("highscores.txt","w")
    highscoreFile.write("99999\n99999\n99999")

def addHighscore(difficulty, score):
    newHighscore = False

    highscoreFile = open("highscores.txt")
    highscores = [float(x) for x in highscoreFile.read().split("\n")]

    if score < highscores[difficulty]:
        highscores[difficulty] = score
        newHighscore = True

    highscoreFile = open("highscores.txt", "w")
    highscoreFile.write("\n".join([str(x) for x in highscores]))

    return newHighscore

def getHighscores():
    highscoreFile = open("highscores.txt")
    highscores = highscoreFile.read().split("\n")

    for i in range(len(highscores)):
        if highscores[i] in ("99999","99999.0"):
            highscores[i] = "-"

    return highscores