from lib.GameLogic.Grid import GridDrawer
from lib.GameLogic.PieceManager import PieceManager

class PreviewManager:
    def __init__(self, previewSurface, pieceManager):
        self.prevPos = [(1,1),(1,5),(1,9)]
        self.prevGrid = GridDrawer(6, 13,20, 1, (51,51,51))
        self.prevGrid.draw()
        self.surface = previewSurface
        self.pm = pieceManager

