import random
from lib.GameLogic.Tetrispiece import Tetrispiece
from lib.GameLogic.Tetrispiece import Piece

class PieceManager:
    __shapeMap = {Piece.I: [(0, 0), (1, 0), (2, 0), (3, 0)], 
                    Piece.O: [(0, 0), (0, 1), (1, 0), (1, 1)],
                    Piece.T: [(0, 0), (1, 0), (2, 0), (1, 1)],
                    Piece.S: [(1, 0), (2, 0), (0, 1), (1, 1)],
                    Piece.Z: [(0, 0), (1, 0), (1, 1), (2, 1)],
                    Piece.J: [(0, 0), (0, 1), (1, 1), (2, 1)],
                    Piece.L: [(2, 0), (0, 1), (1, 1), (2, 1)]}

    def __init__(self, gm):
        self.bag =  list(PieceManager.__shapeMap.values())
        random.shuffle(self.bag)
        self.nextIndex = 0
        self.gm = gm
        
    def giveNextPiece(self):
        nextShape = self.bag[self.nextIndex]
        if self.nextIndex + 1 < len(PieceManager.__shapeMap):
            print("Currentindex: ", self.nextIndex)
            self.nextIndex += 1
        else:
            self.nextIndex = 0
            random.shuffle(self.bag)
            print("reset!")

        return Tetrispiece(self.gm, nextShape)


        

