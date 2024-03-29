# Externals
import sys
import os
import pygame
import pygame._sdl2.controller

from pygame import Surface
from time import gmtime, strftime
from enum import Enum

# Internals
import framework.Resources as resources
from framework.Grid import Grid
from framework.GameWindow import GameWindow
from framework.BlockRandomizer import BlockRandomizer
from framework.Game import Game
from framework.SaveManager import jsonify_game_data, save_on_file, load_file

timerActive = False


class Rooms(Enum):
    MainMenu = 1
    GameScreen = 2
    GameOver = 4
    QUIT = 3

def button_clicked(mouse_x,
                   mouse_y,
                   button_x,
                   button_y,
                   button_width,
                   button_height):
    x_check_passed = False
    y_check_passed = False
    if ((mouse_x > button_x) and (mouse_x < button_x + button_width)):
        x_check_passed = True

    if ((mouse_y > button_y) and (mouse_y < button_y + button_height)):
        y_check_passed = True

    if ((x_check_passed is True) and (y_check_passed is True)):
        return True
    else:
        return False

class GameOverMenu():
    def __init__(self):
        menu_font = resources.DEFAULT_FONT

        self.gameOverText = menu_font.render(
            'GAME OVER', True, resources.RED, False)
        self.gameOverTextRect = self.gameOverText.get_rect().move(
            ((screen_width/2) - (self.gameOverText.get_width()/2)),
            ((screen_height/2) - (self.gameOverText.get_height()/2)))
        self.leaveHintText = menu_font.render(
            'Press Escape to go to Main Menu', True, resources.GRAY, False)
        self.leaveHintTextRect = self.leaveHintText.get_rect().move(
            (screen_width/2) - (self.leaveHintText.get_width()/2),
            (((screen_height/2) + 64) - (self.leaveHintText.get_height()/2)))

    def draw_menu(self):
        game_over_surface.blits(blit_sequence=(
            (self.gameOverText, self.gameOverTextRect),
            (self.leaveHintText, self.leaveHintTextRect)))

class MainMenu:
    def __init__(self):
        menu_font = resources.DEFAULT_FONT

        self.titleText = menu_font.render(
            'Pytris', True, resources.WHITE, False)
        self.titleTextRect = self.titleText.get_rect().move(
            ((screen_width/2) - (self.titleText.get_width()/2)),
            ((screen_height/6) - (self.titleText.get_height()/2)))
        self.highscoreText = menu_font.render(
            'Highscore: 0', True, resources.WHITE, False)
        self.highscoreTextRect = self.highscoreText.get_rect().move(
            ((screen_width/2) - (self.highscoreText.get_width()/2)),
            ((screen_height/6) + self.highscoreText.get_height()))
        self.startText = menu_font.render(
            'Start', True, resources.WHITE, False)
        self.startTextRect = self.startText.get_rect().move(
            ((screen_width) - (self.startText.get_width() + 64)),
            (((screen_height/6)*2) - (self.startText.get_height()/2)))
        self.continueTextWhite = menu_font.render(
            'Continue', True, resources.WHITE, False)
        self.continueTextGray = menu_font.render(
            'Continue', True, resources.GRAY, False)
        self.continueTextRect = self.continueTextWhite.get_rect().move(
            ((screen_width) - (self.continueTextWhite.get_width() + 64)),
            (((screen_height/6)*3) - (self.continueTextWhite.get_height()/2)))
        self.exitText = menu_font.render('Exit', True, resources.WHITE, False)
        self.exitTextRect = self.exitText.get_rect().move(
            ((screen_width) - (self.titleText.get_width() + 64)),
            (((screen_height/6)*4) - (self.titleText.get_height()/2)))

    def draw_menu(self):
        menu_surface.blits(blit_sequence=(
            (self.titleText, self.titleTextRect),
            (self.startText, self.startTextRect),
            (self.highscoreText, self.highscoreTextRect),
            (self.exitText, self.exitTextRect)))

        if gameStarted:
            menu_surface.blit(self.continueTextWhite, self.continueTextRect)
        else:
            menu_surface.blit(self.continueTextGray, self.continueTextRect)

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

    def check_continue_text_click(self, x, y):
        text = self.continueTextWhite
        text_rect = self.continueTextRect
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

    def update(self):
        menu_font = resources.DEFAULT_FONT

        self.highscoreText = menu_font.render(
            "Highscore: " + str(player.highscore), True, resources.WHITE, False)
        self.highscoreTextRect = self.highscoreText.get_rect().move(
            ((screen_width/2) - (self.highscoreText.get_width()/2)),
            ((screen_height/6) + self.highscoreText.get_height()))


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


class Empty:
    pass

def gameend_event_hander(event):
    global gameState, gameStarted

    if event.type == pygame.QUIT:
        exitProcess()
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_ESCAPE:
            gameState = Rooms.MainMenu


def menu_event_handler(event):
    global gameState, gameStarted

    if event.type == pygame.QUIT:
        exitProcess()
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            position = event.pos

            x = position[0]
            y = position[1]

            tstart_clicked = mmenu.check_start_text_click(x, y)
            if (tstart_clicked is True):
                gameStarted = True
                start_game()
                gameState = Rooms.GameScreen

            tcontinue_clicked = mmenu.check_continue_text_click(x, y)
            if(tcontinue_clicked is True):
                if gameStarted:
                    gameState = Rooms.GameScreen

            texit_clicked = mmenu.check_exit_text_click(x, y)
            if (texit_clicked is True):
                exitProcess()


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
        exitProcess()
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
            obj_list.currentBlock.rotateCheck(gridObj.displayGrid)
        if event.key == pygame.K_UP:
            obj_list.currentBlock.instantDown(gridObj.displayGrid)
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
        'Score - ' + str(player.score), True, resources.WHITE, False)
    ui_surface.blit(scoreText, scoreText.get_rect().move(0, 7))


def start_game():
    gridObj.reset()
    startBlock = blockRandomizer.getRandomBlock()
    obj_list.new_block(startBlock)
    player.score = 0


def exitProcess():
    jsonDat = jsonify_game_data(
        game.gameDataPath, gridObj, player, obj_list, gameStarted)
    save_on_file(game.gameDataPath, jsonDat)

    pygame.quit()
    sys.exit()

def load_previous_data():
    global gameStarted
    if os.path.exists(game.gameDataPath+"/save.json"):
        try:

            gridDict, playerDict, objectListDict, blkIndex, started = load_file(
                    game.gameDataPath+"/save.json")

            gridObj.__dict__ = gridDict
            player.__dict__ = playerDict
            obj_list.__dict__ = objectListDict

            e = blockRandomizer.findBlockType(blkIndex)
            Blanky = e(5, 0)
            Blanky.__dict__ = obj_list.currentBlock
            obj_list.currentBlock = Blanky
            gameStarted = started
        except:
            return

"""
def draw_a_grid(tile_size=16, horiz_padding=0, vert_padding=0):
    for x in range(0+horiz_padding, screen_width-horiz_padding, tile_size):
        for y in range(0+vert_padding, screen_height-vert_padding, tile_size):
            rect = pygame.Rect(x, y, tile_size, tile_size)
            pygame.draw.rect(screen, WHITE, rect, 1)
"""

pygame.init()

# Display setup
screen_width = 640
screen_height = 840
resolution = screen_width, screen_height
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Pytris - The Block Game")

gridObj = Grid(48, screen_width, screen_height,
               vert_padding=32, horiz_padding=32)

# Initializes Surfaces
grid_surface = Surface((screen_width, screen_height))
ui_surface = Surface((screen_width, screen_height))
menu_surface = Surface((screen_width, screen_height))
game_over_surface = Surface((screen_width, screen_height))

game = Game()
gameState = Rooms.MainMenu
gameStarted = False

controller = Empty()
if pygame._sdl2.controller.get_count():
    controller = pygame._sdl2.controller.Controller()

# Loads in Main Menu
mmenu = MainMenu()
gomenu = GameOverMenu()

blockRandomizer = BlockRandomizer()
startBlock = blockRandomizer.getRandomBlock()
obj_list = ObjectList(startBlock)

player = Player()

gameClock = pygame.time.Clock()

load_previous_data()
mmenu.update()

while True:
    while gameState == Rooms.MainMenu:
        mmenu.update()

        for event in pygame.event.get():
            menu_event_handler(event)

        screen.fill(resources.BLACK)
        menu_surface.fill(resources.BLACK)

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
            if rowsCleared == 4:
                player.score += 500
            else:
                player.score += (100 * rowsCleared)

            newBlock = blockRandomizer.getRandomBlock()
            obj_list.new_block(newBlock)
            if not obj_list.currentBlock.can_spawn(gridObj.grid):
                gameStarted = False
                gameState = Rooms.GameOver
                player.highscore = player.score

        if timerActive is False:
            pygame.time.set_timer(pygame.USEREVENT, 1000)
            timerActive = True

        screen.fill(resources.BLACK)
        grid_surface.fill(resources.BLACK)
        ui_surface.fill(resources.BLACK)
        ui_surface.set_colorkey(resources.BLACK)

        draw_grid(gridObj.displayGrid)
        draw_ui()

        screen.blits(blit_sequence=(
            (grid_surface, grid_surface.get_rect()),
            (ui_surface, ui_surface.get_rect())))

        gameClock.tick(120)

        pygame.display.flip()
    while gameState == Rooms.GameOver:
        for event in pygame.event.get():
            gameend_event_hander(event)

        screen.fill(resources.BLACK)
        game_over_surface.fill(resources.BLACK)

        gomenu.draw_menu()

        screen.blit(game_over_surface, game_over_surface.get_rect())
        gameClock.tick(120)

        pygame.display.flip()
