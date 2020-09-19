import pygame
import time
from lib.GameLogic.FpsTimer import FpsTimer
from lib.GameLogic.Grid import GridDrawer
from lib.GameItems.Block import Block

pygame.init()

pygame.display.set_caption("Tetris")

screen_x = 500
screen_y = 600
screen = pygame.display.set_mode((screen_x, screen_y))
screen.fill((0, 0, 255))
pygame.display.update()

grid = GridDrawer(10, 20, 20, 1,(51, 51, 51)) #Traditional tetris is 10 by 20
x,y = grid.getBlockSize()

tetris_surface = grid.surface
block = Block(tetris_surface,x,y,x)
fpsClock = FpsTimer(time.time(), 60)  # running @ 60fps

running = True
cntr = 0

keyBlock = {pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_SPACE}
while running:
    # TODO:
    # Make a feature branch
    # Start the main-game module here
    # Check ordering of drawing element, can it be simplified?
    # Maybe add some block control in de the grid? --> Someone has to manage the state of the blocks
    cntr += 1
    tetris_surface.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in keyBlock:
                block.doKey(event.key)
                pass
            elif event.key == pygame.K_ESCAPE:
                running = False

    block.draw()
    grid.draw()

    screen.blit(tetris_surface, (100, (screen_y - tetris_surface.get_height())/2))
    pygame.display.update()
    fpsClock.endFrame()
