class tile:
    def __init__(self,isMine,isShown,defaultTexture,isFlagged):
        self.isMine = isMine
        self.isShown = isShown
        self.texture = defaultTexture
        self.isFlagged = isFlagged

class presets:
    empty = tile(False,False,9,False)
    mine = tile(True,False,9,False)