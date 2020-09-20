import pygame
from lib.GameLogic.Gridblock import Gridblock

class Gridmanager:
    #Manages the grid, the blocks, drawing and game logic

    def __getBlockList(self, x, y):
        grid = []
        squareX, squareY = self.grid.getBlockSize()

        for row in range(0, y):
            rowList = []

            for column in range(0, x):
                rowList.append(Gridblock(column * squareX, row * squareY, squareX))

            grid.append(rowList)

        return grid
    
    #TODO: create blocks, rows and assign position + size to them
    #TODO: implement drawing logic
    def __init__(self, grid):
        self.grid = grid
        self.x_nr, self.y_nr = grid.getGridSize()
        self.blockList = self.__getBlockList(self.x_nr, self.y_nr)

    def drawAll(self):
        #First draw the blocks
        for row in self.blockList:
            for block in row:
                block.draw(self.grid.surface)

        self.grid.draw() #Overwrite with the grid lines