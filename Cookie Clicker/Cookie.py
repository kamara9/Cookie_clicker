import pygame
from Item import *


class Cookie(Item):
    def __init__(self, screen, color, position, size):
        super().__init__(screen, color, position, size)
        self.screen = screen
        self.position = position
        self.size = size
        self.color = color

    def draw_cookie(self, color, position, size):
        pygame.draw.rect(self.screen, color, pygame.Rect(position[0], position[1], size[0], size[1]))
