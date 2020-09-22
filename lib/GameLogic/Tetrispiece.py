from enum import Enum

class Piece(Enum):
    I = 0
    O = 1
    T = 2
    S = 3
    Z = 4
    J = 5
    L = 6


pieceList = {Piece.I: [(0, 0), (1, 0), (2, 0), (3, 0)],
             Piece.O: [(0, 0), (0, 1), (1, 0), (1, 1)],
             Piece.T: [(0, 0), (1, 0), (2, 0), (1, 1)],
             Piece.S: [(1, 0), (2, 0), (0, 1), (1, 1)],
             Piece.Z: [(0, 0), (1, 0), (1, 1), (2, 1)],
             Piece.J: [(0, 0), (0, 1), (1, 1), (2, 1)],
             Piece.L: [(2, 0), (0, 1), (1, 1), (2, 1)]}


class Movement(Enum):
    left = 0,
    right = 1,
    down = 2,
    bottom = 3,


class Tetrispiece:

    def __init__(self, gameManager):

        # TODO: Move piece selection to contructor
        self.shape = pieceList[Piece.L]
        self.pos = (4, 17) 
        self.surface = None
        self.gm = gameManager

    def setSurface(self, surface):
        self.surface = surface

    def draw(self):
        self.gm.drawPiece()


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
