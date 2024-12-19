class Tile:
    def __init__(self):
        self.isMine = False
        self.isShown = False
        self.texture = 0
        self.isFlagged = False

    def changeTexture(self,to):
        self.texture = to
