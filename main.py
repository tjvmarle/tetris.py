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

tetris_x = 200
tetris_y = tetris_x / 10 * 24
tetris_surface = pygame.Surface((tetris_x, tetris_y))
grid = GridDrawer(tetris_surface, 10, 24, 1, (51, 51, 51))
x,y = grid.getBlockSize()
block = Block(tetris_surface,x+1,y+1,x)
fpsClock = FpsTimer(time.time(), 60)  # running @ 60fps

running = True
cntr = 0
while running:
    # Make a feature branch
    # Start the main-game module here
    # Add butten handling --> Esc == quit
    # Check ordering of drawing element, can it be simplified?
    # First determine grid parameters, then determine drawing surface dimensions
    cntr += 1
    tetris_surface.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            running = False

    if cntr % 10 == 0:
        block.moveDown()

    block.draw()
    grid.draw()

    screen.blit(tetris_surface, (100, (screen_y - tetris_y)/2))
    pygame.display.update()
    fpsClock.endFrame()
