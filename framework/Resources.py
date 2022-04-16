import pygame


assetsFolder = 'assets'
EMPTY_TILE = pygame.image.load(assetsFolder + '/tile.png')
TILE_FILLED = pygame.image.load(assetsFolder + '/tilefilled.png')

pygame.font.init()

DEFAULT_FONT = pygame.font.Font(None, 28)
