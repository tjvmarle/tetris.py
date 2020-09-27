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
        if self.status == status and self.color != color:
            return

        if status == Blockstatus.active and not color:
            raise Exception("Activating a non-active block requires a color")

        self.status = status

        if not color:
            if status == Blockstatus.empty:
                # TODO: add background color to constructor
                self.color = (0, 0, 0)
            elif status == Blockstatus.passive:  # Only active and color-containing blocks should be able to turn passive
                newRgb = []
                for newClr in self.color:
                    newClr = newClr - 155 if newClr - 155 > 0 else 0
                    newRgb.append(newClr)

                self.color = tuple(newRgb)
        else:
            self.color = color

        self.draw()

        # TODO: make some logic to add shadows to colored blocks
