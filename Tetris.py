import pygame
import time
from lib.GameLogic.FpsTimer import FpsTimer

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tetris")
screen.fill((0, 0, 255))
pygame.display.update()

fpsClock = FpsTimer(time.time(), 60)  # running @ 60fps

countdown = 120

running = True
while running:
    # Start some game logic module here
    # Next: Draw a grid on the screen

    countdown -= 1

    if countdown == 0:
        running = False

    pygame.display.flip()
    fpsClock.endFrame()
