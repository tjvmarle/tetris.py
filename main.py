import pygame
import time

from pygame.event import wait
from lib.GameLogic.FpsTimer import FpsTimer
from lib.GameLogic.Grid import GridDrawer
from lib.GameLogic.Gamemanager import Gamemanager
from lib.GameLogic.PreviewManager import PreviewManager

# TODO:
# Refactor structure
# Maybe seperate logic and surface management --> easier to blit a single list later
# Simplify de Gamemanager, delegate more to other classes

pygame.init()

pygame.display.set_caption("Tetris")

screen_x = 500
screen_y = 600
screen = pygame.display.set_mode((screen_x, screen_y))
screen.fill((0, 0, 255))
pygame.display.update()

# Traditional tetris is 10 by 20
grid = GridDrawer(10, 20, 20, 1, (51, 51, 51))
gm = Gamemanager(grid)
fpsClock = FpsTimer(time.time(), 60)  # running @ 60fps

previewSurface = pygame.Surface((150, 300))
prevm = PreviewManager(previewSurface, gm.pm)
gm.prevManager = prevm

running = True
cntr = 0

keyBlock = {pygame.K_LEFT, pygame.K_RIGHT,
            pygame.K_DOWN, pygame.K_SPACE, pygame.K_RCTRL}

# grid.surface.fill((0, 0, 0))
gm.drawAll()

while running:
    # TODO: Start the main-game module here

    cntr += 1

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in keyBlock:
                gm.move(event.key)
            elif event.key == pygame.K_ESCAPE:
                running = False

    if cntr % 15 == 0:
        running = gm.tick()

    y_offset = int((screen_y - grid.surface.get_height())/2)

    screen.blit(grid.surface, (50, y_offset))
    # TODO: Implement some surface manager to blit all the relevant surfaces
    screen.blit(prevm.prevGrid.surface, (300, y_offset))
    pygame.display.update()

    if running:
        fpsClock.endFrame()
    else:
        # Plays small game-over 'animation'
        while(gm.gameOver()):
            screen.blit(grid.surface, (50, y_offset))
            pygame.display.update()


time.sleep(1)
