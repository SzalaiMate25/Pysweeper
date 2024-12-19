class tile:
    def __init__(self,isMine,isShown,defaultTexture,isFlagged):
        self.isMine = isMine
        self.isShown = isShown
        self.texture = defaultTexture
        self.isFlagged = isFlagged

    def changeTexture(self,to):
        self.texture = to

class presets:
    empty = tile(False,False,9,False)
    mine = tile(True,False,9,False)
    flagged = tile(False,False,10,True)