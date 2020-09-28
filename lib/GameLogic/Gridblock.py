from enum import Enum
import pygame
import random


class Blockstatus(Enum):
    empty = 0
    active = 1
    passive = 2
    dead = 3


# Keeps track of single block in the grid
class Gridblock:

    def __init__(self, x_pos, y_pos, size, surface, bgClr):
        self.x_pos = x_pos  # position in pixels
        self.y_pos = y_pos
        self.status = Blockstatus.empty
        self.size = size
        self.color = (0, 0, 0)
        self.surface = surface
        self.edge = 4
        self.bgColor = bgClr

    def colorShadow(self):
        shadowColor = []
        for clr in self.color:
            shadowColor.append(51) if clr > 0 else shadowColor.append(0)

        return tuple(shadowColor)

    def colorHighlight(self):
        highColor = []
        for clr in self.color:
            highColor.append(255) if clr > 0 else highColor.append(204)

        return tuple(highColor)

    def dim(self, color):
        dimmed = []
        for clr in color:
            dimmed.append(clr - 102)

        return dimmed

    def draw(self):
        if self.status == Blockstatus.active:
            pygame.draw.polygon(self.surface, self.colorHighlight(), ((self.x_pos, self.y_pos), (
                self.x_pos, self.y_pos + self.size), (self.x_pos + self.size, self.y_pos)))
            pygame.draw.polygon(self.surface, self.colorShadow(), ((self.x_pos + self.size, self.y_pos), (
                self.x_pos, self.y_pos + self.size), (self.x_pos + self.size, self.y_pos + self.size)))
            pygame.draw.rect(self.surface, self.color, (self.x_pos + self.edge,
                                                        self.y_pos + self.edge, self.size - 2 * self.edge, self.size - 2 * self.edge))

        elif self.status == Blockstatus.passive:
            pygame.draw.polygon(self.surface, self.dim(self.colorHighlight()), ((self.x_pos, self.y_pos), (
                self.x_pos, self.y_pos + self.size), (self.x_pos + self.size, self.y_pos)))
            pygame.draw.polygon(self.surface, self.colorShadow(), ((self.x_pos + self.size, self.y_pos), (
                self.x_pos, self.y_pos + self.size), (self.x_pos + self.size, self.y_pos + self.size)))
            pygame.draw.rect(self.surface, self.color, (self.x_pos + self.edge,
                                                        self.y_pos + self.edge, self.size - 2 * self.edge, self.size - 2 * self.edge))

        else:
            pygame.draw.rect(self.surface, self.color,
                             (self.x_pos, self.y_pos, self.size, self.size))

    def Status(self, status, color=None):
        if self.status == status and self.color == color:  # Nothing to change
            return

        if status == Blockstatus.active and not color:
            raise Exception("Activating a non-active block requires a color")

        self.status = status

        if not color:
            if status == Blockstatus.empty:
                # TODO: add background color to constructor
                self.color = (0, 0, 0)
            # Only active and color-containing blocks should be able to turn passive #Wrong!
            elif status == Blockstatus.passive:
                newRgb = []
                for newClr in self.color:
                    newClr = newClr - 155 if newClr - 155 > 0 else 0
                    newRgb.append(newClr)

                self.color = tuple(newRgb)
        else:
            self.color = color

        self.draw()
