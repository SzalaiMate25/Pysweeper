class Tile:
    def __init__(self,isMine,isShown):
        self.isMine = isMine
        self.isShown = isShown
        self.texture = None

    def changeTexture(self,to):
        self.texture = to
