import sys
import os
# import random
import pygame
from pygame import Surface
from time import gmtime, strftime
from Game.Grid import Grid
from Game.GameWindow import GameWindow
from Game.Game import Game
from Game.Block import Block


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


objectList = []


class Player:
    def __init__(self):
        self.highscore = 0


class ObjectList:
    def __init__(self, startingBlock):
        self.objects = []
        self.objects.append(startingBlock)
        self.currentBlockIndex = 0
        self.currentBlock = self.objects[self.currentBlockIndex]

    def new_block(self, block):
        self.objects.append(block)
        self.currentBlockIndex += 1
        self.currentBlock = self.objects[self.currentBlockIndex]


class TestBlock(Block):
    def __init__(self, *args):
        super().__init__(*args)
        self.shape = [[True, True],
                      [True, True]]


def draw_grid(grid):
    for row in grid:
        for tile in row:
            if tile[2] is True:
                grid_surface.blit(spr_tile_filled, (tile[0], tile[1]))
            else:
                grid_surface.blit(spr_tile, (tile[0], tile[1]))


def create_grid(tile_size=16, horiz_padding=0, vert_padding=0):
    myGrid = []
    for y in range(0+vert_padding, screen_height-(vert_padding*2), tile_size):
        currentRow = []
        for x in range(0+horiz_padding, screen_width-horiz_padding, tile_size):
            gridItem = [x, y, False]
            currentRow.append(gridItem)
        myGrid.append(currentRow)
    return myGrid


"""
def draw_a_grid(tile_size=16, horiz_padding=0, vert_padding=0):
    for x in range(0+horiz_padding, screen_width-horiz_padding, tile_size):
        for y in range(0+vert_padding, screen_height-vert_padding, tile_size):
            rect = pygame.Rect(x, y, tile_size, tile_size)
            pygame.draw.rect(screen, WHITE, rect, 1)
"""

pygame.init()

screen_width = 640
screen_height = 840
resolution = screen_width, screen_height
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Shady Block Game")

spr_tile = pygame.image.load("Assets/tile.png")
spr_tile_filled = pygame.image.load("Assets/tilefilled.png")

theGrid = create_grid(tile_size=48, vert_padding=32, horiz_padding=32)
gridObj = Grid(theGrid)

grid_surface = Surface((screen_width, screen_height))
gameStuff = Game()

testBlock = TestBlock(theGrid, 5, 1)
gameClock = pygame.time.Clock()
timerActive = False

while True:
    gridObj.clear_grid()

    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            if testBlock.isFalling:
                testBlock.yOffset += 1
                testBlock.getBottomSide()
                testBlock.isFalling = testBlock.canMoveDown(
                    gridObj.displayGrid)
                timerActive = False
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F12:
                path = gameStuff.gameDataPath + "/screenshots/" + \
                    strftime('%d_%b_%Y_%H_%M_%S', gmtime()) + ".png"

                pygame.image.save(screen, path)
            if event.key == pygame.K_LEFT:
                if testBlock.isFalling:
                    testBlock.xOffset -= 1
            if event.key == pygame.K_RIGHT:
                if testBlock.isFalling:
                    testBlock.xOffset += 1
            if event.key == pygame.K_DOWN:
                if testBlock.isFalling:
                    testBlock.yOffset += 1
                    testBlock.isFalling = testBlock.canMoveDown(
                        gridObj.displayGrid)

    testBlock.paste_on_grid(gridObj.displayGrid)

    if timerActive is False:
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        timerActive = True

    # Refreshes the screen with the blank black background
    screen.fill(BLACK)
    grid_surface.fill(BLACK)

    draw_grid(gridObj.displayGrid)
    screen.blit(grid_surface, grid_surface.get_rect())

    # Draws a grid
    # draw_a_grid(tile_size=48, vert_padding=32, horiz_padding=32)

    # Essentially pastes the testBlock onto the screen at x,y (100,00)
    # screen.blit(testBlock.sprite, (100, 100))

    # Required for displaying stuff on screen
    # Essentially a 'Draw function'

    gameClock.tick(120)

    pygame.display.flip()
