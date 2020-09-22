import random
from lib.GameLogic.Tetrispiece import Tetrispiece
from lib.GameLogic.Tetrispiece import Piece

class PieceManager:
    __pieceList = {Piece.I: [(0, 0), (1, 0), (2, 0), (3, 0)], 
        Piece.O: [(0, 0), (0, 1), (1, 0), (1, 1)],
        Piece.T: [(0, 0), (1, 0), (2, 0), (1, 1)],
        Piece.S: [(1, 0), (2, 0), (0, 1), (1, 1)],
        Piece.Z: [(0, 0), (1, 0), (1, 1), (2, 1)],
        Piece.J: [(0, 0), (0, 1), (1, 1), (2, 1)],
        Piece.L: [(2, 0), (0, 1), (1, 1), (2, 1)]}

    def __init__(self, gm):
        self.bag = PieceManager.__pieceList.copy() #Shallow copy is fine
        random.shuffle(self.bag) #FIXME: maps are unordered, can't acces by index.
        self.nextIndex = 0
        self.gm = gm
        
    def giveNextPiece(self):
        nextShape = self.bag[0]
        if self.nextIndex + 1 < len(PieceManager.__pieceList):
            self.nextIndex += 1
        else:
            self.nextIndex = 0
            random.shuffle(self.bag)

        return Tetrispiece(self.gm, nextShape)


        

