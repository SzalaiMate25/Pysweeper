import tile
import random

class map:
    def __init__(self,size):
        self.map = [[tile.presets.empty for j in range(size)] for i in range(size)]
        self.size = size

    def getAdjacent(self,coords):
        mines = 0
        for i in range(-1,2):
            for j in range(-1,2):
                try:
                    mines += self.map[coords[0]][coords[1]].isMine
                except: pass
        return mines
    
    def countMines(self):
        mines = 0
        for row in self.map:
            mines += (row.count(tile.presets.mine))
        return mines
    
    def placeMines(self,amount):
        while self.countMines() < amount:
            self.map[random.randint(0,self.size - 1)][random.randint(0,self.size - 1)] = tile.presets.mine
