import pygame


class GridDrawer:
    surface = None
    # pygameRef = pygame

    def __init__(self, drawing_surface):
        self.surface = drawing_surface
        print("Surface gezet")

    def draw(self, x_squares, y_squares, line_thickness, line_color):
        x, y = self.surface.get_size()
        square_w = x / x_squares - line_thickness / x_squares
        square_h = y / y_squares - line_thickness / y_squares

        # Draw vertical lines
        for i in range(0, x_squares + 2):
            pygame.draw.line(self.surface, line_color, (square_w * i, 0),
                             (square_w * i, y), line_thickness)

        # Horizontal lines
        for i in range(0, y_squares + 2):
            pygame.draw.line(self.surface, line_color, (0, square_h * i),
                             (x, square_h * i), line_thickness)
