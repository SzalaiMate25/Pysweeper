import tile

class map:
    def __init__(self,size):
        self.map = [[tile() for j in range(size)] for i in range(size)]

    def getAdjacent(self,coords):
        mines = 0
        for i in range(-1,2):
            for j in range(-1,2):
                mines += self.map[coords[0]][coords[1]].isMine
