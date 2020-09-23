from enum import Enum
import random

class Piece(Enum):
    I = 0
    O = 1
    T = 2
    S = 3
    Z = 4
    J = 5
    L = 6


class Movement(Enum):
    left = 0,
    right = 1,
    down = 2,
    bottom = 3,


class Tetrispiece:
                
    def __init__(self, gameManager, shape):
        self.shape = shape
        self.pos = (4, 10) 
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
    
    def move(self, direction):
        if direction == Movement.down:
            self.moveDown()
        else:
            pass
