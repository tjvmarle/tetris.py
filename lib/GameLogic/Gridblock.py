from enum import Enum

class Blockstatus(Enum):
    empty = 0
    active = 1
    passive = 2


#Keeps track of single block in the grid
class Gridblock:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.status = Blockstatus.empty
        self.color = None

    def status(self, status, color = None):
        self.status = status
        self.color = color

    def draw(self):
        if self.color:
            #TODO: draw a square with the right color
            #TODO: make some logic to add shadows to colored blocks