import pygame
import time
from lib.GameLogic.Gridblock import Gridblock
from lib.GameLogic.Gridblock import Blockstatus
from lib.GameLogic.PieceManager import PieceManager


class Gamemanager:
    bgColor = (0, 0, 0)
    # Manages the grid, the blocks, drawing and game logic

    # Index the playing field
    # TODO: There was some kind of Python annotation syntax
    # TODO: Could probably use some major refactoring. Clean up/delegate many of the implementations.
    # TODO: Problably easier to change all colors to lists instead of tuples
    # TODO: Maybe move this to a seperate class to manage the blocks on the playing field
    def __getBlockList(self, x, y):
        grid = []
        squareX, squareY = self.grid.getBlockSize()

        for column in range(0, x):
            rowList = []

            for row in range(0, y):
                rowList.append(
                    Gridblock(column * squareX, row * squareY,
                              squareX, self.grid.surface, Gamemanager.bgColor))

            grid.append(rowList)

        return grid

    def __init__(self, grid):
        self.grid = grid
        self.x_nr, self.y_nr = grid.getGridSize()
        self.blockList = self.__getBlockList(self.x_nr, self.y_nr)
        self.active_piece = None
        self.pm = PieceManager(self)
        self.insertNextPiece()
        self.gameOverFlag = False
        self.prevManager = None

    def gameOver(self):
        for rowNr in range(len(self.blockList[0]) - 1, -1, -1):
            block = None
            for colNr in range(0, len(self.blockList)):
                block = self.blockList[colNr][rowNr]

                if block.status == Blockstatus.passive or block.status == Blockstatus.active:
                    block.Status(Blockstatus.dead, (102, 102, 102))
                    self.grid.draw()
                    time.sleep(0.05)
                    return True

        return False  # All passive block turned dead

    def moveDownAbove(self, rowNr):
        for row in range(rowNr, 0, -1):
            for colNr in range(0, len(self.blockList)):
                aboveBlock = self.blockList[colNr][row - 1]
                self.blockList[colNr][row].Status(
                    aboveBlock.status, aboveBlock.color)

        # Top line can be done seperately
        for colnr in range(0, len(self.blockList)):
            rowBlock = self.blockList[colnr][0]
            rowBlock.Status(Blockstatus.empty)

    def checkLine(self):
        for rowNr in range(0, len(self.blockList[0])):
            clearRow = True

            for colNr in range(0, len(self.blockList)):
                rowBlock = self.blockList[colNr][rowNr]
                if rowBlock.status != Blockstatus.passive:
                    clearRow = False  # No use checking the rest of the line
                    break

            if not clearRow:
                continue

            for colNr in range(0, len(self.blockList)):
                block = self.blockList[colNr][rowNr]
                block.Status(Blockstatus.empty)

            # Immediately move down all blocks above by one line. Waiting for clearing multiple lines at once can become quite complicated.
            self.moveDownAbove(rowNr)

    def deactivatePiece(self, piece):
        x_pos, y_pos = piece.pos
        for block_x, block_y in piece.shape:
            block = self.blockList[block_x + x_pos][block_y + y_pos]
            block.Status(Blockstatus.passive)

        self.checkLine()
        # Check if this moves on the same tick() - could give some erratic behavior at the top
        self.insertNextPiece()

    def insertNextPiece(self):
        self.active_piece = self.pm.giveNextPiece()
        if self.collides(self.active_piece, self.active_piece.pos):  # Game over
            self.gameOverFlag = True

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
        self.drawPiece()
        self.grid.draw()  # Overlay the grid lines

    def tick(self):  # Not actual fps, equals the game's 'playing speed'
        if self.gameOverFlag:
            return False

        self.active_piece.move(pygame.K_DOWN)
        self.drawAll()

        return True
