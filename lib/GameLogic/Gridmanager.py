import pygame
from Gridblock import Gridblock

class Gridmanager:
    #Manages the grid, the blocks, drawing and game logic

    #TODO: create blocks, rows and assign position + size to them
    #TODO: implement drawing logic
    def __init__(self, grid):
        self.grid = grid
        self.x_nr, self.y_nr = grid.getGridSize()