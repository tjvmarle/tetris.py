import pygame
import time
from lib.GameLogic.FpsTimer import FpsTimer
from lib.GameLogic.Grid import GridDrawer
from lib.GameLogic.Gridmanager import Gamemanager
from lib.GameLogic.Tetrispiece import Tetrispiece
from lib.GameLogic.PieceManager import PieceManager 

from lib.GameItems.Block import Block

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
pm = PieceManager(gm)

fpsClock = FpsTimer(time.time(), 60)  # running @ 60fps

running = True
cntr = 0

keyBlock = {pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_SPACE}
fieldChanged = False


while running:
    # TODO:
    # Start the main-game module here

    if cntr == 0:
        grid.surface.fill((0, 0, 0))
        gm.insertPiece(pm.giveNextPiece())
        gm.draw()

    cntr += 1

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in keyBlock:
                #TODO: add left, right and space to tetrispieces
                # Space == moveDown until collision
                pass
            elif event.key == pygame.K_ESCAPE:
                running = False

    if cntr % 30 == 0:
        gm.tick()

    screen.blit(grid.surface, (100, int(
        (screen_y - grid.surface.get_height())/2)))
    pygame.display.update()

    fpsClock.endFrame()
