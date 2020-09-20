import pygame

#TODO: this can probably be deprecated/move to Gridblock
class Block:

    def __init__(self, surf, x_pos, y_pos, width):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.surface = surf
        self.size = width  
        self.keyActions = {pygame.K_LEFT : (-1,0), pygame.K_RIGHT : (1,0), pygame.K_DOWN : (0,1), pygame.K_SPACE : (0,2)}  

    def draw(self):
        if self.surface != None:
            pygame.draw.rect(self.surface, (255,0,0), (self.x_pos, self.y_pos, self.size, self.size))

    def __move(self,delta):
        x, y = delta
        self.x_pos += x * self.size
        self.y_pos += y * self.size
        #TODO: Boundary checking

    def doKey(self, keypressed):
        if keypressed in self.keyActions:
            self.__move(self.keyActions[keypressed])
        pass