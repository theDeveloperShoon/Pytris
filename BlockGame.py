import sys
import pygame

pygame.init()
screen_width = 640
screen_height = 840
resolution = screen_width, screen_height
pygame.display.set_mode(resolution)
pygame.display.set_caption("Shady Block Game")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
