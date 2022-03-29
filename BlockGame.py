import sys
import pygame


class Player:
    def __init__(self):
        self.highscore = 0


class TestBlock:
    def __init__(self):
        self.sprite = pygame.image.load("Assets/TestBlock.png")

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
