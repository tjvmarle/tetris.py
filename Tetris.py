import pygame
import lib.GameLogic.fpsclock

print("Hello testy")

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tetris")
screen.fill((0, 0, 255))
pygame.display.update()

countdown = 1000000

running = True
while running:
    for event in pygame.event.get():
        print(event.type)

    countdown -= 1
    if countdown % 100000 == 0:
        print("Countdown: ", countdown)

    if countdown == 0:
        running = False
