import pygame
import time
from lib.GameLogic.FpsTimer import FpsTimer
from lib.GameLogic.Grid import GridDrawer
from lib.GameLogic.Gridmanager import Gridmanager
from lib.GameItems.Block import Block

pygame.init()

pygame.display.set_caption("Tetris")

screen_x = 500
screen_y = 600
screen = pygame.display.set_mode((screen_x, screen_y))
screen.fill((0, 0, 255))
pygame.display.update()

grid = GridDrawer(10, 20, 20, 1,(51, 51, 51)) #Traditional tetris is 10 by 20
gm = Gridmanager(grid)

fpsClock = FpsTimer(time.time(), 60)  # running @ 60fps

running = True
cntr = 0

keyBlock = {pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_SPACE}
while running:
    # TODO:
    # Start the main-game module here
    # Optimize: Only redraw the field if something changed
    # More optimization: let blocks redraw back to background instead of redrawing entire surface
    cntr += 1
    grid.surface.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in keyBlock:
                # block.doKey(event.key)
                pass
            elif event.key == pygame.K_ESCAPE:
                running = False

    gm.drawAll()

    screen.blit(grid.surface, (100, (screen_y - grid.surface.get_height())/2))
    pygame.display.update()
    fpsClock.endFrame()
