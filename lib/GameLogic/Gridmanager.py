import pygame
from lib.GameLogic.Gridblock import Gridblock
from lib.GameLogic.Gridblock import Blockstatus


class Gridmanager:
    # Manages the grid, the blocks, drawing and game logic

    def __getBlockList(self, x, y):
        grid = []
        squareX, squareY = self.grid.getBlockSize()

        for column in range(0, x):
            rowList = []

            for row in range(0, y):
                rowList.append(
                    Gridblock(column * squareX, row * squareY, squareX, self.grid.surface))

            grid.append(rowList)

        return grid

    # TODO: create blocks, rows and assign position + size to them
    # TODO: implement drawing logic
    def __init__(self, grid):
        self.grid = grid
        self.x_nr, self.y_nr = grid.getGridSize()
        self.blockList = self.__getBlockList(self.x_nr, self.y_nr)
        self.active_piece = None

    def insertPiece(self, piece):
        self.active_piece = piece
        self.active_piece.setSurface(self.grid.surface)
        self.active_piece.draw()

    def drawPiece(self):
        x_pos, y_pos = self.active_piece.pos
        for x_shape, y_shape in self.active_piece.shape:
            block = self.blockList[x_shape + x_pos][y_shape + y_pos]
            block.Status(Blockstatus.active, (255, 0, 0))

    def draw(self):
        # First draw the blocks
        # for row in self.blockList:
        #     for block in row:
        #         block.draw(self.grid.surface)

        self.grid.draw()  # Overlay the grid lines
