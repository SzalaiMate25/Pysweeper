def resetHighscores():
    highscoreFile = open("highscores.txt","w")
    highscoreFile.write("99999\n99999\n99999")

def addHighscore(difficulty, score):
    highscoreFile = open("highscores.txt")
    highscores = [float(x) for x in highscoreFile.read().split("\n")]

    if score < highscores[difficulty]:
        highscores[difficulty] = score

    highscoreFile = open("highscores.txt", "w")
    highscoreFile.write("\n".join([str(x) for x in highscores]))

def getHighscores():
    highscoreFile = open("highscores.txt")
    highscores = highscoreFile.read().split("\n")

    for i in range(len(highscores)):
        if highscores[i] in ("99999","99999.0"):
            highscores[i] = "-"

    return highscores