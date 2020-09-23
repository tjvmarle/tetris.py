import random
import pygame
from enum import Enum

class Piece(Enum):
    I = 0
    O = 1
    T = 2
    S = 3
    Z = 4
    J = 5
    L = 6

class Tetrispiece:
                
    def __init__(self, gameManager, shape):
        self.shape = shape
        self.pos = (4, 0) #TODO maybe change to a list
        self.surface = None
        self.gm = gameManager
        self.clr = random.choice([(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255)])

    def setSurface(self, surface):
        self.surface = surface #TODO: Probably should make this a getter at Gm or set at construction

    def moveDown(self):
        x_pos, y_pos = self.pos
        if not self.gm.collides(self, (x_pos, y_pos + 1)):
            self.gm.drawPiece(True)  # First 'undraw' the piece
            self.pos = (x_pos, y_pos + 1)
            self.gm.drawPiece()  # Redraw on next position
        else:
            self.gm.deactivatePiece(self)

    def moveSide(self, direction):
        x_dir = 1 if direction == pygame.K_RIGHT else -1
        x_pos, y_pos = self.pos
        if not self.gm.collides(self, (x_pos + x_dir, y_pos)):
            self.gm.drawPiece(True)  # First 'undraw' the piece
            self.pos = (x_pos + x_dir, y_pos)
            self.gm.drawPiece()  # Redraw on next position

    def move(self, direction):
        if direction == pygame.K_DOWN:
            self.moveDown()
        elif direction in (pygame.K_LEFT, pygame.K_RIGHT):
            self.moveSide(direction)
        else:
            pass
