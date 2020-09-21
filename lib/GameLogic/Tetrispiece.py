from enum import Enum

# self.shape = [(0, 0), (0, 1), (0, 2), (0, 3)]  # I piece
# self.shape = [(0, 0), (0, 1), (1, 0), (1, 1)]  # O piece
# self.shape = [(0, 0), (0, 1), (0, 2), (1, 1)]  # T piece
# self.shape = [(1, 0), (2, 0), (0, 1), (0, 2)]  # S piece
# self.shape = [(0, 0), (1, 0), (1, 1), (1, 2)]  # Z piece
# self.shape = [(0, 0), (0, 1), (1, 1), (2, 1)]  # J piece
# self.shape = [(2, 0), (0, 1), (1, 1), (2, 1)]  # L piece


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


class Tetrispiece:

    def __init__(self, gridManager):

        # TODO: Move piece selection to contructor
        self.shape = pieceList[Piece.L]
        self.pos = (4, 0)  # Top mid
        self.surface = None
        self.gm = gridManager

    def setSurface(self, surface):
        self.surface = surface

    def draw(self):
        self.gm.drawPiece()
