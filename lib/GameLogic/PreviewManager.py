

class PreviewManager:
    def __init__(self, previewSurface, pieceManager):
        self.surface = previewSurface
        self.pm = pieceManager

        self.surface.fill((0,0,0))
