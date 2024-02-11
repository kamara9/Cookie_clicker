import pygame
from Item import *


class Clicker(Item):
    def __init__(self, screen, color, position, size, price, clicks_per_second, count, name):
        super().__init__(screen, color, position, size)
        self.screen = screen
        self.position = position
        self.size = size
        self.color = color
        self.clicks_per_second = clicks_per_second
        self.count = count
        self.price = price
        self.name = name

    def draw_clicker(self, color, position, size, text=""):
        text_position = [position[0] + 10, position[1] + size[1] / 3.5]
        price_position = [position[0] + 10, position[1] + size[1] / 1.3]
        count_position = [position[0] + size[0] - 50, position[1] + size[1] / 3.5]

        font_large = pygame.font.SysFont("Arial", 20)
        font_small = pygame.font.SysFont("Arial", 12)
        pygame.draw.rect(self.screen, color, pygame.Rect(position[0], position[1], size[0], size[1]))

        name = font_large.render(text, 1, (0, 0, 0))
        price = font_small.render(str(self.price), 1, (0, 0, 0))
        count = font_large.render(str(self.count), 1, (0, 0, 0))

        self.screen.blit(name, text_position)
        self.screen.blit(price, price_position)
        self.screen.blit(count, count_position)

    def buy_clicker(self, cookie_sum):
        cookie_sum -= self.price
        self.raise_price()
        self.count += 1
        return cookie_sum

    def enough_money(self, cookie_sum):
        if (cookie_sum - self.price) >= 0:
            return True

    def raise_price(self):
        self.price *= 2
