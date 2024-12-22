import tile
import random
from copy import deepcopy as copy

class map:
    def __init__(self,size):
        self.map = [[copy(tile.presets.empty) for j in range(size)] for i in range(size)]
        self.size = size

    def getAdjacent(self,coords):
        mines = 0
        for i in range(-1,2):
            for j in range(-1,2):
                try: 
                    if coords[0] + j > -1 and coords[1] + i > -1:
                        mines += self.map[coords[0] + j][coords[1] + i].isMine
                except: pass
        return mines
    
    def countMines(self):
        mines = 0
        for row in self.map:
            for cell in row:
                if cell.isMine:
                    mines += 1
        return mines
    
    def placeMines(self,amount):
        while self.countMines() < amount:
            self.map[random.randint(0,self.size - 1)][random.randint(0,self.size - 1)] = copy(tile.presets.mine)

    def clear(self,coords):
        self.map[coords[0]][coords[1]].texture = self.getAdjacent((coords[0],coords[1]))
        self.map[coords[0]][coords[1]].isShown = True

        if self.map[coords[0]][coords[1]].texture == 0:
            for i in range(-1,2):
                for j in range(-1,2):
                    try:
                        if coords[0] + j > -1 and coords[1] + i > -1 and not self.map[coords[0] + j][coords[1] + i].isShown:
                            self.map[coords[0] + j][coords[1] + i].texture = self.getAdjacent((coords[0] + j,coords[1] + i))

                            if self.map[coords[0] + j][coords[1] + i].texture == 0:
                                self.clear((coords[0] + j,coords[1] + i))
                    except: pass

    def minesLeft(self):
        mines = 0
        for row in self.map:
            for cell in row:
                mines += cell.isMine - cell.isFlagged
        return mines
