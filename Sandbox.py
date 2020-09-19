import pygame

pygame.init()

pygame.display.set_caption("Sandbox")
screen = pygame.display.set_mode((800, 600))
screen.fill((100, 100, 100))
pygame.display.update()
keyPress = {pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_SPACE}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key in keyPress:
            print("Key: ", event.key)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    pygame.display.update()