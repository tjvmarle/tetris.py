from enum import Enum
import pygame
import random


class Blockstatus(Enum):
    empty = 0
    active = 1
    passive = 2

# Keeps track of single block in the grid


class Gridblock:

    def __init__(self, x_pos, y_pos, size, surface):
        self.x_pos = x_pos  # position in pixels
        self.y_pos = y_pos
        self.status = Blockstatus.empty
        self.size = size
        self.color = (0, 0, 0)
        self.surface = surface

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x_pos,
                                                    self.y_pos, self.size, self.size))

    def Status(self, status, color=None):
        if self.status != status:
            self.status = status
            self.color = color if color else (0, 0, 0)
            self.draw()

        # TODO: draw a square with the right color
        # TODO: make some logic to add shadows to colored blocks
