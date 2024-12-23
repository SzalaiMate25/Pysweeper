import time

stopped = False
timer = 0

def startTimer():
    global timer
    global stopped
    global stoppedAt

    timer = time.time()
    stopped = False

def getTimer():
    global timer
    global stopped
    global stoppedAt

    if stopped:
        return stoppedAt
    elif timer == 0:
        return 0
    return time.time() - timer

def stop():
    global timer
    global stopped
    global stoppedAt
    
    stoppedAt = time.time() - timer
    stopped = True

def convertTime(seconds, returnFormat):
    minute = str(int(seconds / 60))
    second = str(int(seconds) % 60)

    if len(minute) == 1:
        minute = "0" + minute

    if len(second) == 1:
        second = "0" + second

    return ((minute, second), f"{minute}:{second}")[returnFormat]