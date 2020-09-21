import pygame
from lib.GameLogic.Gridblock import Gridblock
from lib.GameLogic.Gridblock import Blockstatus
from lib.GameLogic.Tetrispiece import Movement


class Gamemanager:
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

    def drawPiece(self, undraw=False):
        x_pos, y_pos = self.active_piece.pos
        for x_shape, y_shape in self.active_piece.shape:
            block = self.blockList[x_shape + x_pos][y_shape + y_pos]

            if not undraw:
                block.Status(Blockstatus.active, (255, 0, 0))
            else:
                block.Status(Blockstatus.empty, (0, 0, 0))

    def draw(self):
        self.grid.draw()  # Overlay the grid lines

    def collides(self, piece, nextPos):
        for x_block, y_block in piece.shape:
            x_pos, y_pos = nextPos
            x_pos += x_block
            y_pos += y_block

            if y_pos >= self.y_nr:  # Hit the bottom
                return True

            if x_pos <= -1 or x_pos >= self.x_nr:  # Hit the sides
                return True

            gmBlock = self.blockList[x_pos][y_pos]

            if gmBlock.status == Blockstatus.passive:  # Ignore active blocks or you might collide with yourself
                return True

        return False

    def tick(self):  # Not actual fps, equals the game's 'playing speed'
        if self.active_piece:
            self.active_piece.move(Movement.down)
