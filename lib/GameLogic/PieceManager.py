import random
from lib.GameLogic.Tetrispiece import Tetrispiece
from lib.GameLogic.Tetrispiece import Piece


class PieceManager:
    # TODO Should probably change these to matrices and apply some basic math
    __shapeMap = {Piece.I: [[(0, 0), (1, 0), (2, 0), (3, 0)], [(2, -1), (2, 0), (2, 1), (2, 2)], [(0, 1), (1, 1), (2, 1), (3, 1)], [(1, -1), (1, 0), (1, 1), (1, 2)]],
                  Piece.O: [[(0, 0), (0, 1), (1, 0), (1, 1)], [(0, 0), (0, 1), (1, 0), (1, 1)], [(0, 0), (0, 1), (1, 0), (1, 1)], [(0, 0), (0, 1), (1, 0), (1, 1)]],
                  Piece.T: [[(0, 0), (1, 0), (2, 0), (1, 1)], [(1, -1), (0, 0), (1, 0), (1, 1)], [(1, -1), (0, 0), (1, 0), (2, 0)], [(1, -1), (1, 0), (2, 0), (1, 1)]],
                  Piece.S: [[(1, 0), (2, 0), (0, 1), (1, 1)], [(1, 0), (1, 1), (2, 1), (2, 2)], [(1, 1), (2, 1), (0, 2), (1, 2)], [(0, 0), (0, 1), (1, 1), (1, 2)]],
                  Piece.Z: [[(0, 0), (1, 0), (1, 1), (2, 1)], [(2, 0), (1, 1), (2, 1), (1, 2)], [(0, 1), (1, 1), (1, 2), (2, 2)], [(1, 0), (0, 1), (1, 1), (0, 2)]],
                  Piece.J: [[(0, 0), (0, 1), (1, 1), (2, 1)], [(1, 0), (2, 0), (1, 1), (1, 2)], [(0, 1), (1, 1), (2, 1), (2, 2)], [(1, 0), (1, 1), (0, 2), (1, 2)]],
                  Piece.L: [[(2, 0), (0, 1), (1, 1), (2, 1)], [(1, 0), (1, 1), (1, 2), (2, 2)], [(0, 1), (1, 1), (2, 1), (0, 2)], [(0, 0), (1, 0), (1, 1), (1, 2)]]}

    def __init__(self, gm):
        self.bag = list(PieceManager.__shapeMap.values())
        random.shuffle(self.bag)
        self.nextIndex = 0
        self.gm = gm

    def giveNextPiece(self):
        nextShape = self.bag[self.nextIndex]
        if self.nextIndex + 1 < len(PieceManager.__shapeMap):
            self.nextIndex += 1
        else:
            self.nextIndex = 0
            random.shuffle(self.bag)

        return Tetrispiece(self.gm, nextShape, self.gm.grid.surface)
