import pygame
import time
from lib.GameLogic.FpsTimer import FpsTimer
from lib.GameLogic.Grid import GridDrawer

screen_x = 500
screen_y = 600

tetris_x = 200
tetris_y = 500

pygame.init()

screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Tetris")
screen.fill((0, 0, 255))
pygame.display.update()

fpsClock = FpsTimer(time.time(), 60)  # running @ 60fps

tetris_surface = pygame.Surface((tetris_x, tetris_y))
grid = GridDrawer(tetris_surface)


countdown = 120

running = True
while running:
    # Start the main-game module here
    # Add butten handling --> Esc == quit
    # Check ordering of drawing element, can it be simplified?

    grid.draw(10, 24, 1, (51, 51, 51))

    countdown -= 1

    if countdown == 0:
        running = False

    screen.blit(tetris_surface, (100, (screen_y - tetris_y)/2))
    pygame.display.flip()
    fpsClock.endFrame()
