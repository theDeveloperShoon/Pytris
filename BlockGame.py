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


def grid(tile_size=16, horiz_padding=0, vert_padding=0):
    for x in range(0+horiz_padding, screen_width-horiz_padding, tile_size):
        for y in range(0+vert_padding, screen_height-vert_padding, tile_size):
            rect = pygame.Rect(x, y, tile_size, tile_size)
            pygame.draw.rect(screen, WHITE, rect, 1)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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

    grid(tile_size=32, vert_padding=32, horiz_padding=32)
    # Essentially pastes the testBlock onto the screen at x,y (100,00)
    # screen.blit(testBlock.sprite, (100, 100))

    # Required for displaying stuff on screen
    # Essentially a 'Draw function'
    pygame.display.flip()
