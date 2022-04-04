import pygame


class GameWindow:
    def __init__(self, width=600, height=600):
        self.window_width = width
        self.window_height = height

    def set_title(self, title):
        pygame.display.set_caption(title)
