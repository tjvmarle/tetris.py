from enum import Enum
import pygame
import random

class Blockstatus(Enum):
    empty = 0
    active = 1
    passive = 2

#Keeps track of single block in the grid
class Gridblock:
    clr = [(255,0,0),(0,255,0),(0,0,255)]

    def __init__(self, x_pos, y_pos, size):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.status = Blockstatus.empty
        self.size = size
        # self.color = None
        self.color = random.choice(Gridblock.clr)

    def status(self, status, color = None):
        self.status = status
        self.color = color if color else (0,0,0)
        pygame.draw.rect(surface, self.color, (self.x_pos, self.y_pos, self.size, self.size))

    def draw(self, surface): #probably not necessarry anymore with the drawing in status()
        # if self.color:

            #TODO: draw a square with the right color
            #TODO: make some logic to add shadows to colored blocks