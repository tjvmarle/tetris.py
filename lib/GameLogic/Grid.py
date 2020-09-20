import pygame

#TODO: Maybe change into a rectangle-drawer and inherit a square-drawer from it
class GridDrawer:
    # surface = None
    # x_grid = 0
    # y_grid = 0
    # line_thick = 0
    # line_clr = (0,0,0)

    def __init__(self, x_squares, y_squares, square_size, line_thickness, line_color):
        self.surface = pygame.Surface((x_squares * square_size + line_thickness, y_squares * square_size + line_thickness))
        self.line_thick = line_thickness
        self.line_clr = line_color
        self.block_size = square_size
        self.x_nr = x_squares
        self.y_nr = y_squares
        
        
        # x, y = self.surface.get_size()
        # self.x_grid = x / x_squares - line_thickness / x_squares
        # self.y_grid = y / y_squares - line_thickness / y_squares

    def getBlockSize(self):
        return (self.block_size, self.block_size)

    def getSurfaceSize(self):
        return self.surface.get_size()

    def getGridSize(self):
        return (self.x_nr, self.y_nr)
    
    def draw(self):
        x, y = self.surface.get_size()

        #Vertical lines
        for i in range(0, self.x_nr + 1):
            x_pos = i * self.block_size
            pygame.draw.line(self.surface, self.line_clr, (x_pos, 0), (x_pos, y))
        
        #Horizontal lines
        for i in range(0, self.y_nr + 1):
            y_pos = i * self.block_size
            pygame.draw.line(self.surface, self.line_clr, (0, y_pos), (x, y_pos))

