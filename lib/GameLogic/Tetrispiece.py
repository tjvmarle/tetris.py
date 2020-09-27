import random
import pygame
from enum import Enum
from itertools import cycle


class Piece(Enum):
    I = 0
    O = 1
    T = 2
    S = 3
    Z = 4
    J = 5
    L = 6


class Tetrispiece:

    def __init__(self, gameManager, shapeList, surface):
        self.shapeList = cycle(shapeList)
        self.shape = next(self.shapeList)
        self.pos = (4, 0)  # TODO maybe change to a list instead op tuple
        self.surface = surface
        self.gm = gameManager
        self.clr = random.choice(
            [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)])

    def moveDown(self):
        x_pos, y_pos = self.pos
        if not self.gm.collides(self, (x_pos, y_pos + 1)):
            self.gm.drawPiece(True)  # First 'undraw' the piece
            self.pos = (x_pos, y_pos + 1)
            self.gm.drawPiece()  # Redraw on next position
            return True
        else:
            self.gm.deactivatePiece(self)
            return False

    def moveSide(self, direction):
        x_dir = 1 if direction == pygame.K_RIGHT else -1
        x_pos, y_pos = self.pos
        if not self.gm.collides(self, (x_pos + x_dir, y_pos)):
            self.gm.drawPiece(True)  # First 'undraw' the piece
            self.pos = (x_pos + x_dir, y_pos)
            self.gm.drawPiece()  # Redraw on next position

    def spin(self):
        prevShape = self.shape
        self.gm.drawPiece(True)

        self.shape = next(self.shapeList)
        if self.gm.collides(self, self.pos):
            self.shape = prevShape  # TODO: check position 1 to left and/or right and try again

            while(self.shape != next(self.shapeList)):  # Reset the cycle
                pass

        self.gm.drawPiece()

    def move(self, direction):
        if direction == pygame.K_DOWN:
            self.moveDown()
        elif direction in (pygame.K_LEFT, pygame.K_RIGHT):
            self.moveSide(direction)
        elif direction == pygame.K_SPACE:
            self.spin()
        elif direction == pygame.K_RCTRL:
            while(self.moveDown()):
                pass
