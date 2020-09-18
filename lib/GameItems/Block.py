import pygame

class Block:
    x_pos = 0
    y_pos = 0
    size = 0 
    surface = None

    def __init__(self, surf, x_pos, y_pos, width):
        self.x_pos = x_pos +1
        self.y_pos = y_pos
        self.surface = surf
        self.size = width

    def draw(self):
        if self.surface != None:
            pygame.draw.rect(self.surface, (255,0,0), (self.x_pos, self.y_pos, self.size, self.size))

    def moveDown(self):
        self.y_pos += self.size

