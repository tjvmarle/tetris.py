import pygame
from lib.GameLogic.Gridblock import Gridblock
from lib.GameLogic.Gridblock import Blockstatus
from lib.GameLogic.PieceManager import PieceManager


class Gamemanager:
    # Manages the grid, the blocks, drawing and game logic

    # Index the playing field
    # TODO: There was some kind of Python annotation syntax
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

    def __init__(self, grid):
        self.grid = grid
        self.x_nr, self.y_nr = grid.getGridSize()
        self.blockList = self.__getBlockList(self.x_nr, self.y_nr)
        self.active_piece = None
        self.pm = PieceManager(self)
        self.insertNextPiece()

    def deactivatePiece(self, piece):
        x_pos, y_pos = piece.pos
        for block_x, block_y in piece.shape:
            block = self.blockList[block_x + x_pos][block_y + y_pos]
            block.Status(Blockstatus.passive)

        # TODO: Check for filled lines to remove
        self.active_piece = None

    def insertNextPiece(self):
        # TODO: Check for collision at insertion == game lost
        self.active_piece = self.pm.giveNextPiece()

    # TODO: Delegate implementation to the piece itself
    def drawPiece(self, undraw=False):
        x_pos, y_pos = self.active_piece.pos
        for x_shape, y_shape in self.active_piece.shape:
            block = self.blockList[x_shape + x_pos][y_shape + y_pos]

            if not undraw:
                block.Status(Blockstatus.active, self.active_piece.clr)
            else:
                block.Status(Blockstatus.empty, (0, 0, 0))

    def collides(self, piece, nextPos):
        for x_block, y_block in piece.shape:
            x_pos, y_pos = nextPos
            x_pos += x_block
            y_pos += y_block

            if y_pos < 0:  # Hit the top, only relevant for I-piece
                return True

            if y_pos >= self.y_nr:  # Hit the bottom
                return True

            if x_pos <= -1 or x_pos >= self.x_nr:  # Hit the sides
                return True

            collidingBlock = self.blockList[x_pos][y_pos]

            # Ignore active blocks or you might collide with yourself
            if collidingBlock.status == Blockstatus.passive:
                return True

        return False

    def move(self, direction):
        if self.active_piece:
            self.active_piece.move(direction)
            self.grid.draw()  # Lazy but easy

    def drawAll(self):
        # move(DOWN) from tick() could've disabled the piece without inserting a new one
        if self.active_piece:
            # TODO Find something more elegant here. Maybe insert new piece at deactivation
            self.drawPiece()

        self.grid.draw()  # Overlay the grid lines

    def tick(self):  # Not actual fps, equals the game's 'playing speed'
        if self.active_piece:
            self.active_piece.move(pygame.K_DOWN)
        else:
            self.insertNextPiece()

        self.drawAll()
