import pygame


class GridDrawer:
    surface = None
    x_grid = 0
    y_grid = 0
    line_thick = 0
    line_clr = (0,0,0)

    def __init__(self, drawing_surface,x_squares, y_squares, line_thickness, line_color):
        self.surface = drawing_surface
        x, y = self.surface.get_size()
        self.x_grid = x / x_squares - line_thickness / x_squares
        self.y_grid = y / y_squares - line_thickness / y_squares
        self.line_thick = line_thickness
        self.line_clr = line_color

    def getBlockSize(self):
        return (self.x_grid, self.y_grid)
    
    def draw(self):
        x, y = self.surface.get_size()

        # Draw vertical lines
        for i in range(0, int(x/self.x_grid) + 1):
            pygame.draw.line(self.surface, self.line_clr, (self.x_grid * i, 0),
                             (self.x_grid * i, y), self.line_thick)

        # Horizontal lines
        for i in range(0, int(y/self.y_grid) + 1):
            pygame.draw.line(self.surface, self.line_clr, (0, self.y_grid * i),
                             (x, self.y_grid * i), self.line_thick)
