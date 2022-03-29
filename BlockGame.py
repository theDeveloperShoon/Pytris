import sys
import pygame


class Player:
    def __init__(self):
        self.highscore = 0


class ObjectList:
    def __init__(self):
        self.objects = []


class TestBlock:
    def __init__(self):
        self.sprite = pygame.image.load("Assets/TestBlock.png")


BLACK = (0, 0, 0)


pygame.init()
screen_width = 640
screen_height = 840
resolution = screen_width, screen_height
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Shady Block Game")


testBlock = TestBlock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Refreshes the screen with the blank black background
    screen.fill(BLACK)

    # Essentially pastes the testBlock onto the screen at x,y (100,00)
    screen.blit(testBlock.sprite, (100, 100))

    # Required for displaying stuff on screen
    # Essentially a 'Draw function'
    pygame.display.flip()
