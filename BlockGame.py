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
timerActive = False


class Rooms(Enum):
    MainMenu = 1
    GameScreen = 2
    QUIT = 3


class MainMenu:
    def __init__(self):
        menu_font = resources.DEFAULT_FONT

        self.titleText = menu_font.render('Pytris', True, WHITE, False)
        self.titleTextRect = self.titleText.get_rect().move(
            ((screen_width/2) - (self.titleText.get_width()/2)),
            ((screen_height/6) - (self.titleText.get_height()/2)))
        self.startText = menu_font.render('Start', True, WHITE, False)
        self.startTextRect = self.startText.get_rect().move(
            ((screen_width/2) - (self.startText.get_width()/2)),
            (((screen_height/6)*2) - (self.startText.get_height()/2)))
        self.exitText = menu_font.render('Exit', True, WHITE, False)
        self.exitTextRect = self.exitText.get_rect().move(
            ((screen_width/2) - (self.titleText.get_width()/2)),
            (((screen_height/6)*4) - (self.titleText.get_height()/2)))

    def draw_menu(self):
        menu_surface.blit(self.titleText, self.titleTextRect)
        menu_surface.blit(self.startText, self.startTextRect)
        menu_surface.blit(self.exitText, self.exitTextRect)

    def check_title_text_click(self, x, y):
        text = self.titleText
        text_rect = self.titleTextRect
        text_width = text.get_width()
        text_height = text.get_height()
        text_x = text_rect.x
        text_y = text_rect.y

        return button_clicked(x, y, text_x, text_y, text_width, text_height)

    def check_start_text_click(self, x, y):
        text = self.startText
        text_rect = self.startTextRect
        text_width = text.get_width()
        text_height = text.get_height()
        text_x = text_rect.x
        text_y = text_rect.y

        return button_clicked(x, y, text_x, text_y, text_width, text_height)

    def check_exit_text_click(self, x, y):
        text = self.exitText
        text_rect = self.exitTextRect
        text_width = text.get_width()
        text_height = text.get_height()
        text_x = text_rect.x
        text_y = text_rect.y

        return button_clicked(x, y, text_x, text_y, text_width, text_height)


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


def menu_event_handler(event):
    global gameState

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            position = event.pos

            x = position[0]
            y = position[1]

            tstart_clicked = mmenu.check_start_text_click(x, y)
            if (tstart_clicked is True):
                gameState = Rooms.GameScreen

            texit_clicked = mmenu.check_exit_text_click(x, y)
            if (texit_clicked is True):
                pygame.quit()
                sys.exit()


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
        'Score - ' + str(player.score), True, WHITE, False)
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
menu_surface = Surface((screen_width, screen_height))
game = Game()
gameState = Rooms.MainMenu

# Loads in Main Menu
mmenu = MainMenu()

blockRandomizer = BlockRandomizer()
startBlock = blockRandomizer.getRandomBlock()
obj_list = ObjectList(startBlock)


player = Player()

gameClock = pygame.time.Clock()

while True:
    while gameState == Rooms.MainMenu:
        for event in pygame.event.get():
            menu_event_handler(event)

        screen.fill(BLACK)
        menu_surface.fill(BLACK)

        mmenu.draw_menu()

        screen.blit(menu_surface, menu_surface.get_rect())
        gameClock.tick(120)

        pygame.display.flip()
    while gameState == Rooms.GameScreen:
        gridObj.update()

        for event in pygame.event.get():
            game_event_handler(event)

        gridObj.displayGrid = obj_list.currentBlock.paste_on_grid(
            gridObj.displayGrid)

        if obj_list.currentBlock.isFalling is False:
            gridObj.fall_procedure()

            rowsCleared = gridObj.amountOfClearsinLastProcedure
            player.score += (50 * rowsCleared)

            newBlock = blockRandomizer.getRandomBlock()
            obj_list.new_block(newBlock)

        if timerActive is False:
            pygame.time.set_timer(pygame.USEREVENT, 1000)
            timerActive = True

        screen.fill(BLACK)
        grid_surface.fill(BLACK)
        ui_surface.fill(BLACK)
        ui_surface.set_colorkey(BLACK)

        draw_grid(gridObj.displayGrid)
        draw_ui()

        screen.blits(blit_sequence=(
            (grid_surface, grid_surface.get_rect()),
            (ui_surface, ui_surface.get_rect())))

        gameClock.tick(120)

        pygame.display.flip()
