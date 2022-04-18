# Externals
import sys
import os
import pygame
from pygame import Surface
from time import gmtime, strftime
from enum import Enum

# Internals
import framework.Resources as resources
from framework.Grid import Grid
from framework.GameWindow import GameWindow
from framework.BlockRandomizer import BlockRandomizer
from framework.Game import Game


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


objectList = []
class Rooms(Enum):
    MainMenu = 1
    GameScreen = 2
    QUIT = 3


    def __init__(self):


class Player:
    def __init__(self):
        self.highscore = 0
        self.score = 0


class ObjectList:
    def __init__(self, startingBlock):
        self.objects = []
        self.objects.append(startingBlock)
        self.currentBlockIndex = 0
        self.currentBlock = self.objects[self.currentBlockIndex]

    def new_block(self, block):
        self.objects.append(block)
        self.objects.pop(0)
        self.currentBlock = self.objects[self.currentBlockIndex]







def game_event_handler(event):
    global timerActive, gameState

    if event.type == pygame.USEREVENT:
        if obj_list.currentBlock.isFalling:
            if obj_list.currentBlock.canMoveDown(
                    gridObj.displayGrid):
                obj_list.currentBlock.yOffset += 1
            else:
                obj_list.currentBlock.isFalling = False
            timerActive = False
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F12:
            path = game.gameDataPath + "/screenshots/" + \
                strftime('%d_%b_%Y_%H_%M_%S', gmtime()) + ".png"

            pygame.image.save(screen, path)
        if event.key == pygame.K_LEFT:
            if obj_list.currentBlock.isFalling:
                if obj_list.currentBlock.canMoveLeft(gridObj.displayGrid):
                    obj_list.currentBlock.xOffset -= 1
        if event.key == pygame.K_RIGHT:
            if obj_list.currentBlock.isFalling:
                if obj_list.currentBlock.canMoveRight(gridObj.displayGrid):
                    obj_list.currentBlock.xOffset += 1
        if event.key == pygame.K_DOWN:
            if obj_list.currentBlock.isFalling:
                if obj_list.currentBlock.canMoveDown(
                        gridObj.displayGrid):
                    obj_list.currentBlock.yOffset += 1
                else:
                    obj_list.currentBlock.isFalling = False
        if event.key == pygame.K_r:
            obj_list.currentBlock.shape = obj_list.currentBlock.rotate()
            pass
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_ESCAPE:
            gameState = Rooms.MainMenu


def draw_grid(grid):
    for row in grid:
        for tile in row:
            if tile[2] is True:
                grid_surface.blit(resources.TILE_FILLED, (tile[0], tile[1]))
            else:
                grid_surface.blit(resources.EMPTY_TILE, (tile[0], tile[1]))


def draw_ui():
    font = resources.DEFAULT_FONT
    scoreText = font.render(
        'Score - ' + str(myPlayer.score), True, WHITE, False)
    ui_surface.blit(scoreText, scoreText.get_rect())


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
pygame.display.set_caption("Pytris - The Shady Block Game")

gridObj = Grid(48, screen_width, screen_height,
               vert_padding=32, horiz_padding=32)

grid_surface = Surface((screen_width, screen_height))
ui_surface = Surface((screen_width, screen_height))
gameStuff = Game()

blockRandomizer = BlockRandomizer()
startBlock = blockRandomizer.getRandomBlock()
obj_list = ObjectList(startBlock)


myPlayer = Player()

gameClock = pygame.time.Clock()
timerActive = False

while True:
    gridObj.update()

